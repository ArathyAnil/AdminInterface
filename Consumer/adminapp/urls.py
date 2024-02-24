from django.urls import path
from .views import userLogin,logoutUser,customerInvoiceList,addEntry,editCustomer,deleteCustomer,editInvoice,deleteInvoice

urlpatterns = [
    path('',userLogin,name='login-user'),
    path('logout',logoutUser,name='logout-user'),
    path('dashboard',customerInvoiceList,name='sections-dashboard'),
    path('add',addEntry,name='add-entry'),
    path('edit-customer/<int:id>',editCustomer,name='edit-cust'),
    path('delete-customer/<int:id>',deleteCustomer,name='delete-cust-entry'),
    path('edit-invoice/<int:id>',editInvoice,name='edit-invoice'),
    path('delete-invoice/<int:id>',deleteInvoice,name='delete-invoice-entry'),

]