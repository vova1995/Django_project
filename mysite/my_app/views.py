from django.shortcuts import render
# from django.http import HttpResponse



def home(request):
	
	# return HttpResponse('<h1>Hello' + name + '</h1>')
	context = {

	}
	return render(request, 'my_app/home.html', context)