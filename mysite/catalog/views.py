from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .models import Catalog


def catalog_home(request):
	context = {
		'catalog': Catalog.objects.all()
	}
	return render(request, 'catalog/catalog.html', context)

def catalog_detail(request, catalog_id):
	catalog_item = get_object_or_404(Catalog, pk=catalog_id)
	context = {
		'catalog_item': catalog_item,
	}
	return render(request, 'catalog/catalog_detail.html', context)
	# return HttpResponse("Catalog detail page " + catalog_id)