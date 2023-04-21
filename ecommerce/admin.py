from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "category", "description"]
    list_filter = ["category"]
    list_editable = ["price", "category", "description"]

admin.site.register(Product, ProductAdmin)

