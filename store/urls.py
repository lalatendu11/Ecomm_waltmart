from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('product/<int:pk>', views.product, name='product'),#pk = > passing primary key to url
    path('category/<str:foo>', views.category, name='category'), # foo => passing string to url
path('cart_auth/', views.cart_auth, name="cart_auth"),

]
