from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.core.mail import EmailMessage

from .models import Comeisu
# Create your views here.

def productos(request):

	comeisu = Comeisu.objects.all()

	paginator = Paginator(comeisu, 20)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	contexto = {
		'comeisu': page_obj
	}

	return render(request, 'general/products.html',contexto)

def verProducto(request, id):
	comeisu = Comeisu.objects.get(cla_isu = id)

	contexto = {
		'comeisu':comeisu
	}

	return render(request,'general/product.html',contexto)

def send():
	email_message = EmailMessage(
		'Mensaje de usuario',
		'body',
		to=['jonathanch1991@gmail.com'],
	)
	email_message.content_subtype = 'html'
	email_message.send()

	return redirect('')