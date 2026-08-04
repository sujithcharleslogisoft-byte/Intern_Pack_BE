from django.db import models

# Create your models here.
# Creating Category Model Table 
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']
        
    def __str__(self):
        return self.name    
    
    
# Creating Product Model
class product(models.Model):
    title = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(unique=True)  
    description = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.PROTECT,related_name="products")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
        