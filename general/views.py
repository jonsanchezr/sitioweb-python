from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'general/index.html', {'title':'title'})

def product(request):
    return render(request, 'general/product.html', {'title':'Product'})

def products(request):
    return render(request, 'general/products.html', {'title':'Products'})

def sitemap(request):
	return render(request, 'general/sitemap.xml', {
        'text': 'text',
    }, content_type='application/xhtml+xml')

def google(request):
    return render(request, 'general/googleec4d9ed38b3f9dba.html', {'title':'google'})