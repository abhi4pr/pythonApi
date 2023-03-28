from rest_framework import serializers
from .models import Post
from .models import Customer

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','description','date','post_img','author']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name','email','password','address','phone']

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['email','password']