# from django.db import models
# from django.contrib.auth import get_user_model
# from django.utils.translation import gettext_lazy as _


# User = get_user_model()


# class Customer(models.Model):

#     id = models.BigAutoField(primary_key=True,editable=False, unique=True)
#     user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='api_customer',null=False,blank=False)
#     name = models.CharField(max_length=255,null=False,blank=False)
#     phone = models.CharField(max_length=15,null=True,blank=True)
#     email = models.EmailField(max_length=255,null=True,blank=True)
#     Address = models.CharField(max_length=255,null=True,blank=True)


# #Payment choices
# class PaymentStatus(models.TextChoices):

#     UNPAID = "Unpaid",_("Unpaid")
#     PAID = "Paid",_("Paid")
#     CANCELLED = "Cancelled",_("Cancelled")



# #Invoice model
# class Invoice(models.Model):

#     id = models.BigAutoField(primary_key=True,editable=False, unique=True)
#     user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='api_invoice',null=False,blank=False)
#     customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='customer_invoice_api',null=False,blank=False)
#     date = models.DateField(null=True,blank=True)
#     amount = models.FloatField(default=0.0,null=True,blank=True)
#     Status = models.CharField(max_length=10,default='Unpaid',choices=PaymentStatus.choices)

#     def __str__(self):
#         return str(self.id)