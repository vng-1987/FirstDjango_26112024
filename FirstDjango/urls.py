from django.urls import path
from MainApp import views

urlpatterns = [
	path('', views.home),
	path('about/', views.about),
	path('items/', views.items),
	path('items/<int:id>', views.items),
]
