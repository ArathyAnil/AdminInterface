from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

# Create your models here.

#user model 
class User(AbstractUser):

    id = models.UUIDField(primary_key=True,default=uuid4,null=False,blank=False,unique=True,editable=False)
    username = models.CharField(max_length=255,blank=False,null=False,unique=True)
    password = models.CharField(max_length=20,null=False,blank=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["password"]
    def __str__(self):
        return str(self.id)

 


#Payment choices
class PaymentStatus(models.TextChoices):

    UNPAID = "Unpaid",_("Unpaid")
    PAID = "Paid",_("Paid")
    CANCELLED = "Cancelled",_("Cancelled")


class ModelClass(models.TextChoices):

    CUSTOMER = "Customer",_("Customer")
    INVOICE = "Invoice",_("Invoice")



#Invoice model
class TestModel(models.Model):

    id = models.BigAutoField(primary_key=True,editable=False, unique=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='admin_invoice',null=False,blank=False)
    customer = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='customer_entry', null=True, blank=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    phone = models.CharField(max_length=15,null=True,blank=True)
    email = models.EmailField(max_length=255,null=True,blank=True)
    Address = models.CharField(max_length=255,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    amount = models.FloatField(default=0.0,null=True,blank=True)
    Status = models.CharField(max_length=10,default='UNPAID',choices=PaymentStatus.choices,null=True,blank=True)
    type = models.CharField(max_length=10,choices=ModelClass.choices)

    def __str__(self):
        return str(self.id)
    
    def clean(self):

        super().clean()
        print(self.type)
        if self.type == ModelClass.INVOICE:
            print(self.type)
            if not all([self.date,self.amount,self.customer,self.Status]):
                raise ValidationError({
                    'date': 'This field is required for invoices.',
                    'amount': 'This field is required for invoices.',
                    'customer': 'This field is required for invoices.',
                    'Status': 'This field is required for invoices.'
                })  
            self.phone = ''
            self.email = ''
            self.Address = ''
            self.name = ''

        elif self.type == ModelClass.CUSTOMER:
            if not all([self.name, self.phone, self.email, self.Address]):
                raise ValidationError({
                    'name': 'This field is required for customers.',
                    'phone': 'This field is required for customers.',
                    'email': 'This field is required for customers.',
                    'Address': 'This field is required for customers.',
                })
            self.customer = None
            self.date = None
            self.amount = None
            self.Status = ''  
