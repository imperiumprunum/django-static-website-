from django.urls import path
from printer2 import views

urlpatterns = [
	path('printer2', views.render_printer2),
]