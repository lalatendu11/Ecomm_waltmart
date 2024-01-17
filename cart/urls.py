from django.urls import path
from . import views
# from .views import address1

urlpatterns = [
	path('', views.cart_summary, name="cart_summary"),
	path('add/', views.cart_add, name="cart_add"),
	path('delete/', views.cart_delete, name="cart_delete"),
	path('update/', views.cart_update, name="cart_update"),
	path('checkout/', views.checkout, name="checkout"),
path('address', views.address, name="address"),
# path('address1', address1.as_view(),name="address1"),
path('success/', views.success, name="success"),
]
