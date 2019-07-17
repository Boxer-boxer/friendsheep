from django.shortcuts import render, redirect

from catalogo.models import produto
from .models import Cart

# Create your views here.

def cart_home(request):
	cart_obj, new_obj = Cart.objects.new_or_get(request)

	context = {
		'cart': cart_obj,
	}

	return render(request, 'checkout/cart_home.html', context)

def cart_home_update(request):
	produto_id = request.POST.get('produto_id')

	if produto_id is not None:
		try:
			obj = produto.objects.get(id=produto_id)
		except produto.DoesNotExist:
			messages = f'Parece que algo correu mal, por favor tente outra vez mais tarde.'
			return redirect('homepage')

		cart_obj, new_obj = Cart.objects.new_or_get(request)

		if obj in cart_obj.products.all():
			cart_obj.products.remove(obj)
		else:
			cart_obj.products.add(obj)

	return redirect('cart')



