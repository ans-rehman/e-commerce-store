from django.contrib import admin
from .models import Product

# Register your models here.
class productadmin(admin.ModelAdmin):
    list_display = ['product_name', 'category', 'price', 'pub_date', 'status']
    list_editable = ['status','price',]
    
admin.site.register(Product, productadmin)
