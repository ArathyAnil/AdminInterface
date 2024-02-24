from django.shortcuts import render
from .serializers import MyTokenObtainPairSerializer,CustomerSerializer,InvoiceSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from adminapp.models import Customer,Invoice
from rest_framework.generics import UpdateAPIView
# Create your views here.


#login using simple-jwt tokens(POST request)
class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


#POST api for inserting entries into customer and invoice tables
class CreateCustomerInvoiceAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):

        customer_serializer = CustomerSerializer(data=request.data)
        invoice_serializer = InvoiceSerializer(data=request.data)
        print(invoice_serializer)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return Response(customer_serializer.data,status=status.HTTP_201_CREATED)
        elif invoice_serializer.is_valid():
            invoice_serializer.save()
            return Response(invoice_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response({'error':'Invalid Data'},status=status.HTTP_400_BAD_REQUEST)
        

#list all the entries in customer and invoice sectiona based on the parameter passed(GET request)
class ListCustomerInvoiceAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):

        type = request.query_params.get('type')

        if type == 'CUSTOMER':

            customerlist = Customer.objects.filter(user=request.user)
            serializer = CustomerSerializer(customerlist,many=True)
            return Response({'data':serializer.data},status=status.HTTP_200_OK)
        
        if type == 'INVOICE':

            invoiceList = Invoice.objects.filter(user=request.user)
            serializer = InvoiceSerializer(invoiceList,many=True)
            return Response({'data':serializer.data},status=status.HTTP_200_OK)

        return Response({'error':'Invalid Data'},status=status.HTTP_400_BAD_REQUEST)


#partially updating only the required fields without changing other fields - PATCH request
class UpdateCustomerAPIView(UpdateAPIView):

    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()


#partially updating only the required fields without changing other fields - PATCH request
class UpdateInvoiceAPIView(UpdateAPIView):

    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]
    queryset = Invoice.objects.all()





        