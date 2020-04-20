from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'general/index.html', {'title':'title'})

def product(request):
    return render(request, 'general/product.html', {'title':'Product'})