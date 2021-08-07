from django.shortcuts import render

# Create your views here.
def render_printer2(request):
	return render(request, 'printer2.html', {})
