from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate,login
from django.contrib import messages,auth
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import get_object_or_404
from .models import User,TestModel,ModelClass
from django.urls import reverse_lazy
# # Create your views here.

# USER AUTHENTICATION SECTION


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
            return redirect(dashboardView)
        
    return render(request,'login.html',{'formData':formData})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/login")
def logoutUser(request):

    if request.session:
        auth.logout(request)
        return redirect(userLogin)


# #DASHBOARD SECTION
    
# fn for displaying dashbord section 
@login_required(login_url="/login")
def dashboardView(request):

    if request.user.is_authenticated and request.user.is_superuser:
        logged_user = request.user.username
        choices = [choice.value for choice in ModelClass]
        customers = TestModel.objects.filter(user=request.user,type='Customer').count()
        invoice = TestModel.objects.filter(user=request.user,type='Invoice').count()
        return render(request,'admin.html',{'logged_user':logged_user,'customers':customers,'invoices':invoice,'choices':choices})

#fn to create update and list the created customers and invoices
class TestModelView(View):

    model = TestModel

    def get(self, request, section=None, pk=None):

        existing_customers = TestModel.objects.filter(user=request.user, type='Customer').values()
        choices = [choice.value for choice in ModelClass]
        instance = None
        if pk:
            instance = get_object_or_404(self.model, pk=pk)
            return render(request, 'updateEntry.html', {'instance': instance, 'existing_customers': existing_customers, 'choices': choices})

        section = request.GET.get('section', '')

        if section:
            sectionList = TestModel.objects.filter(user=request.user, type=section).values('name', 'phone', 'email', 'Address', 'customer__name', 'date', 'amount', 'Status', 'id')
            return render(request, 'List_entry.html', {'sectionList': sectionList, 'choices': choices})

        return render(request, 'add_entry.html', {'existing_customers': existing_customers, 'choices': choices})


    def post(self, request,pk=None):
        choices = [choice.value for choice in ModelClass]
        data = request.POST 

        existing_customers = TestModel.objects.filter(user=request.user, type='Customer').values()

        if data.get('customer'):
            if TestModel.objects.filter(id=data.get('customer')).exists():
                customer_instance = TestModel.objects.get(id=data.get('customer')).id
            else:

                messages.error(request, "Customer does not exist.")
                return render(request, 'add_entry.html', {'existing_customers': existing_customers})
        else:

            customer_instance = None

        if data.get('pk'):

            instance = get_object_or_404(self.model, pk=data.get('pk'))

            instance.user_id = request.user.id
            instance.customer_id = customer_instance
            instance.name = data.get('name')
            instance.phone = data.get('phone')
            instance.email = data.get('email')
            instance.Address = data.get('address')
            instance.date = data.get('date')
            instance.amount = data.get('amount')
            instance.Status = data.get('status')

            try:
                instance.full_clean()

            except Exception as e:
                messages.error(request, str(e))
                return render(request, 'updateEntry.html', {'instance': instance, 'existing_customers': existing_customers, 'choices': choices})
            
            instance.save()

            messages.success(request, "Entry edited successfully")
            return render(request, 'updateEntry.html', {'instance': instance, 'existing_customers': existing_customers, 'choices': choices})
        
        else:

            instance = TestModel(
                user_id=request.user.id,
                customer_id=customer_instance,
                name=data.get('name'),
                phone=data.get('phone'),
                email=data.get('email'),
                Address=data.get('address'),
                date=data.get('date'),
                amount=data.get('amount'),
                Status=data.get('status'),
                type=data.get('type')
            )
            
            try:
                instance.full_clean()
            except Exception as e:
                messages.error(request, str(e))
                return render(request, 'add_entry.html', {'existing_customers': existing_customers, 'choices': choices})
            instance.save()
            messages.success(request, "Entry added succesfully")
            return render(request, 'add_entry.html', {'existing_customers': existing_customers, 'choices': choices})
        

    
    

