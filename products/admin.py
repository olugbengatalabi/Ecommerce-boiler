from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
  list_display = ["title","price", "featured", "category","quantity available"]
  list_display_links = ["title"]
  list_display_editable = ["featured"]
  
  list_filter = ["title", "price", "featured"]

admin.site.register(Product)

# Register your models here.
