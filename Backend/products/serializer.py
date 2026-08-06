from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category, product

###===== Authentication Serializer ======###
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
###=========Category Serializer========###
class CategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = ['id','name','image']
        
        
###========Product Serializer (for list view/detail/create/update======###
class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField( source="category.name",read_only=True)              ##for these read the category name because the DE stores the ID in Products 
    class Meta():
        model = product
        fields = ['id', 'title', 'price', 'quantity', 'category', 'category_name', 'image']
        
    ####========Validations (price/quantity)============#
    def validate_price(self, value):
        """Check that price is greater than 0"""
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value
    
    def validate_quantity(self, value):
        """Check that quantity is not negative"""
        if value < 0:
            raise serializers.ValidationError("Quantity cannot be negative.")
        return value       