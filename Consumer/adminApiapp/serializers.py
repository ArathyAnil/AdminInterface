
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from adminapp.models import Customer,Invoice

User = get_user_model()

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    class Meta:
        model = User
        fields = ['username','password']

    

    @classmethod
    def get_token(cls, user):

        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        return token  
    
    def validate(self, attrs):

        data = super().validate(attrs)
        data['username'] = self.user.username
        data['id'] = self.user.id
        return data 
    


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:

        model = Customer
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:

        model = Invoice
        fields = '__all__'