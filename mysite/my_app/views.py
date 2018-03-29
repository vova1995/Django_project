from django.shortcuts import render
from catalog.models import Catalog
from datetime import date


def home(request):
	
	# return HttpResponse('<h1>Hello' + name + '</h1>')

	context = {
		# 'currentdate': date,

		'catalog': Catalog.objects.all()[:8],

	}
	return render(request, 'my_app/home.html', context)

