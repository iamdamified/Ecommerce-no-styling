from .models import Product
from django import forms



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = ["name", "description", "category", "price", "image" ] # This allows you to specify the fields you need in your form
        fields = "__all__" # USe this when you do not want to specify the needed fields for your form, you want all of them.