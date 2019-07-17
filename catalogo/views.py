from django.shortcuts import render, get_object_or_404

from .models import produto

# Create your views here.

#Catalogo
def catalogo(request):
	produtos = produto.objects.all()
	context = {
		'produtos': produtos,
	}
	return render(request, 'catalogo/catalogo.html', context)

#Details
def catalogo_produto(request, id):
	produto_detalhe = get_object_or_404(produto, pk=id)

	context = {
		'produto': produto_detalhe,
	}

	return render(request, 'catalogo/produto_detalhe.html', context)
