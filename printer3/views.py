from django.shortcuts import render

# Create your views here.
def render_printer1(request):
	return render(request, 'printer1.html', {})
