from django.urls import path
from .views import MyObtainTokenPairView,CreateCustomerInvoiceAPIView,UpdateCustomerAPIView,UpdateInvoiceAPIView,ListCustomerInvoiceAPIView

urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'), #
    path('create/',CreateCustomerInvoiceAPIView.as_view(),name='customer-invoice-create'), # based on the inputs it will return results. give the customer fields along with logged in user id for creating a customer n similiarly for the creation of an invoice.
    path('list/',ListCustomerInvoiceAPIView.as_view(),name='list-sections'), #give params as type=CUSTOMER or type=INVOICE
    path('update-cust/<int:pk>/',UpdateCustomerAPIView.as_view(),name='customer-partial-update'), # give the id of entry which needs to be editted inplace of <int:id>
    path('update-inv/<int:pk>/',UpdateInvoiceAPIView.as_view(),name='invoice-partial-update')  # give the id of entry which needs to be editted inplace of <int:id>
]