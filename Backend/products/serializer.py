# from django.contrib.auth.models import User
# from rest_framework import serializers
# from .models import Category, product

# ###===== Authentication Serializer ======###
# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)
    
# ###=========Category Serializer========###
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta():
#         model = Category
#         fields = ['id','name','image']
        
        
# ###========Product Serializer (for list view======###
# class ProductListSerailizer(serializers.ModelSerailizer):
           