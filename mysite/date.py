from django.shortcuts import render

def name(request):
	context = 'Hello world'
	return render(request, 'base.html', context)