from django.shortcuts import render

from product.models import Product

def frontpage(request):
    newest_products = Product.objects.all()[0:8]

    return render(request, 'frontpage.html', {'newest_products': newest_products})

def contact(request):
    return render(request, 'contact.html')

def aboutus(request):
    return render(request, 'aboutus.html')