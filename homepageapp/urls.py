from django.urls import path
from homepageapp import views

urlpatterns = [
	path('', views.render_home_page)
]