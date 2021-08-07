from django.urls import path
from printer3 import views

urlpatterns = [
	path('printer3', views.render_printer3),
]