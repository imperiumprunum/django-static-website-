from django.urls import path
from printer1 import views

urlpatterns = [
	path('', views.render_printer1),
]