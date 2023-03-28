from django.http import JsonResponse
from .models import Customer
from .serializers import CustomerSerializer
from .serializers import LoginSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# for generating access token
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'access': str(refresh.access_token),
    }

@api_view(['POST'])
def register(request):
    serialize = CustomerSerializer(data=request.data)
    if serialize.is_valid():
        serialize.save()
        return Response(serialize.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialize.errors)
    
@api_view(['POST'])
def login(request):
    serialize = LoginSerializer(data=request.data)
    if serialize.is_valid():
        email = serialize.data.get('email')
        passw = serialize.data.get('password')
        try:
            user = Customer.objects.filter(email=email, password=passw).first()
            if user:
                gtoken = get_tokens_for_user(user)
                return Response({'sms':'success','data':{'name':user.name,'email':user.email}, 'token':gtoken})
            else:
                return Response({'sms': 'invalid password'})
        except Customer.DoesNotExist:
            return Response({'sms':'no user'})
    else:
        return Response(serialize.errors)
    
@api_view(['GET'])
def profile(request, email):
    try:
        singleuser = Customer.objects.get(email=email)
        serialize = CustomerSerializer(singleuser)
        return Response(serialize.data)
    except Customer.DoesNotExist:
        return Response({'error':'Email Id not found in DB'})