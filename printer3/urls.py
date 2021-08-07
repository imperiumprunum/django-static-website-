from django.urls import path
from printer3 import views

urlpatterns = [
	path('', views.render_printer3),
]