from django.contrib import admin
from .models import Category,Product   #Brand
# Register your models here.

# Create the admin Register 
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    search_fields = ['name',]
    list_filter = ['created_at',]
    ordering = ['name',]
    
#Create The admin Brnad
# @admin.register(Brand)
# class BrandAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'created_at']
#     search_fields = ['name',]
#     list_filter = ['created_at',]
#     ordering = ['name',]
        
    
# Create the admin Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','category','price','quantity']
    search_fields = ['title','description']
    list_filter = ['category']
    ordering = ['-created_at']