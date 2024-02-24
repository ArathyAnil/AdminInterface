from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate,login
from django.contrib import messages,auth
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .models import User,Customer,Invoice
from datetime import datetime
# Create your views here.

#USER AUTHENTICATION SECTION


def userLogin(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    formData = {'username':username,'password':password}
    
    if request.method == 'POST':

        user = authenticate(request,username=username,password=password)

        if user is None:

            messages.error(request,'Wrong username/password')
            return render(request,'login.html',{'formData':formData})
        
        if user.is_active and user.is_superuser:

            login(request,user)
            return redirect(customerInvoiceList)
        
    return render(request,'login.html',{'formData':formData})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/login")
def logoutUser(request):

    if request.session:
        auth.logout(request)
        return redirect(userLogin)


#DASHBOARD SECTION
    
# fn for displaying customer, invoice and dashbord sections combined based on parameter passed 
@login_required(login_url="/login")
def customerInvoiceList(request):

    if request.user.is_authenticated and request.user.is_superuser:

        section = request.GET.get('section','')

        if section == 'customer':
            existing_customers = Customer.objects.filter(user=request.user).values()
            return render(request,'customer.html',{'existing_customers':existing_customers})
        
        if section=='invoice':
            existing_invoice = Invoice.objects.filter(user=request.user).values('customer__name','date','amount','Status','id')
            return render(request,'invoice.html',{'existing_invoice':existing_invoice})
        logged_user = request.user.username
        customers = Customer.objects.filter(user=request.user).count()
        invoice = Invoice.objects.filter(user=request.user).count()
        return render(request,'admin.html',{'logged_user':logged_user,'customers':customers,'invoices':invoice})


#fn for adding a new customer/invoice(combined) works based on the parameter passed   
@login_required(login_url="/login")
def addEntry(request):

    if request.user.is_authenticated and request.user.is_superuser:

        new_addition = request.GET.get('user','')

        if new_addition == 'add-customer':

            name = request.POST.get('name_c')
            phone = request.POST.get('phone_c')
            email = request.POST.get('email_c')
            address = request.POST.get('address_c')

            form_data = {'name':name,'phone':phone,'email':email,'address':address}

            if request.method == 'POST':
                
                adduser = Customer(user=request.user,
                                   name=name,
                                   phone=phone,
                                   email=email,
                                   Address=address)
                adduser.save()

                redirect_url = reverse(customerInvoiceList) + '?section=customer'
                return redirect(redirect_url)
            
            return render(request,'add_customer.html',{})
        
        if new_addition == 'add-invoice':

            customer = request.POST.get('customer_i')
            date = request.POST.get('date_i','1990-01-01')
            amount = request.POST.get('amount_i')
            status = request.POST.get('status_i')

            existing_customers = Customer.objects.filter(user=request.user).values('name','id')

            if request.method == 'POST':

                customer_instance  = Customer.objects.get(id=customer)

                addinvoice = Invoice(customer=customer_instance,
                                     user=request.user,
                                     date=date,
                                     amount=amount,
                                     Status=status)
                addinvoice.save()

                redirect_url = reverse(customerInvoiceList) + '?section=invoice'
                return redirect(redirect_url)
            
            return render(request,'add_invoice.html',{'existing_customers':existing_customers})
        

#fn to edit an existing customer entry
@login_required(login_url="/login")
def editCustomer(request,id):

    if request.user.is_authenticated and request.user.is_superuser:

        entry = Customer.objects.get(user=request.user, id=id)

        name = request.POST.get('name_e')
        phone = request.POST.get('phone_e')
        email = request.POST.get('email_e')
        address = request.POST.get('address_e')

        existing_vals = Customer.objects.filter(id=id).values()
        
        if request.method == 'POST':

            entry.name = name
            entry.phone = phone
            entry.email = email
            entry.Address = address
            entry.save()

            redirect_url = reverse(customerInvoiceList) + '?section=customer'
            return redirect(redirect_url)
        
        return render(request,'edit_customer.html',{'form_data':existing_vals[0]})


#fn to delete an existing customer entry
@login_required(login_url="/login")
def deleteCustomer(request,id):

    if request.user.is_authenticated and request.user.is_superuser:

        entry = Customer.objects.filter(user=request.user, id=id)
        entry.delete()

        redirect_url = reverse(customerInvoiceList) + '?section=customer'
        return redirect(redirect_url)


#fn to edit an existing invoice entry
@login_required(login_url="/login")
def editInvoice(request,id):

    if request.user.is_authenticated and request.user.is_superuser:

        entry = Invoice.objects.get(user=request.user, id=id) 

        customer = request.POST.get('customer_e')
        date = request.POST.get('date_e','1990-01-01')
        amount = request.POST.get('amount_e')
        status = request.POST.get('status_e')

        existing_vals = Invoice.objects.filter(id=id).values()

        for vals in existing_vals:
            vals["date"] = datetime.strftime(vals["date"],'%Y-%m-%d')

        existing_customers = Customer.objects.filter(user=request.user).values('name','id')

        if request.method == 'POST':

            customer_instance  = Customer.objects.get(id=customer)
            entry.customer = customer_instance
            entry.date = date
            entry.amount = amount
            entry.Status = status
            entry.save()

            redirect_url = reverse(customerInvoiceList) + '?section=invoice'

            return redirect(redirect_url)
        return render(request,'edit_invoice.html',{'form_data':existing_vals[0],'existing_customers':existing_customers})


#fn to delete an existing invoice entry
@login_required(login_url="/login")
def deleteInvoice(request,id):

    if request.user.is_authenticated and request.user.is_superuser:

        entry = Invoice.objects.filter(user=request.user, id=id)
        entry.delete()

        redirect_url = reverse(customerInvoiceList) + '?section=invoice'
        return redirect(redirect_url)