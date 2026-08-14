from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category,Product  #Brand

###===== Authentication Serializer ======###
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
###=========Category Serializer========###
class CategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = ['id','name','image']
        
        
# class BrandSerializer(serializers.ModelSerializer):
#     class Meta():
#         model = Brand
#         fields = ['id','name','discount']
                
        
###========Product Serializer (for list view/detail/create/update======###
class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField( source="category.name",read_only=True)              ##for these read the category name because the DE stores the ID in Products
    #brand_name = serializers.CharField(source="brand.name",read_only=True) 
    class Meta():
        model = Product
        fields = [ 'id','title','price', 'quantity','description', 'category','category_name','image']  #'brand_name', 
        
        
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
    
    
    def validate_discount(self, value):
        if value > 100:
            raise serializers.ValidationError("Discount must be between 0 and 100 percent.")
        return value
    
    # def validate_image(self, value):
    #     print(value)
    #     if  value.size < 500 :
    #         raise serializers.ValidationError("Image size must be lessthan 500 KB")
    #     return value  