from django.shortcuts import render

# Create your views here.
def render_printer3(request):
	return render(request, 'printer3.html', {})
