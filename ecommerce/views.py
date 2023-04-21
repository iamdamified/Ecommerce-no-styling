from django.shortcuts import render
from .models import Product
from .forms import ProductForm
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    product = Product.objects.all()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)#collect data
        if form.is_valid(): #validate data
            form.save() # save data
            return HttpResponse("Your product was successfully created")
    else:
        form = ProductForm()

    context = {
        'product_list': product,
        'myform': form
    }
    return render(request, "the/home.html", context)

def aboutPage(request):
    return render(request, "the/about.html")

def productDetailPage(request,pk):
    product = Product.objects.get(id=pk)
    context = {
        'oneproduct': product
    }

    return render(request, "the/productdetail.html", context)
