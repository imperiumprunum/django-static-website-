from django.urls import path
from printer2 import views

urlpatterns = [
	path('', views.render_printer2),
]