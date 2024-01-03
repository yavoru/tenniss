from django.urls import path# import path function from django.urls module
from . import views # import views module from current directory
urlpatterns = [
	path('products/', views.members, name='products'),
	path('products/details/<int:id>', views.details, name='details'),
	path('products/find-new', views.findNew, name='find-new'),
	path('products/testuu',views.testing, name="test"),
	path('',views.main, name="main"),
]

