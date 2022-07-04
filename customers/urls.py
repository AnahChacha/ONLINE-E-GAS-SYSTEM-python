from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('customers/<str:pk>/', views.customers ,name="customer"),
    path('product/', views.products, name="product"),
    path('aboutus/', views.aboutus),
    path('createOrder/', views.createOrder_form ,name="create-order"),
    path('updateOrder/<str:pk>', views.updateOrder ,name="update-order"),
    path('deleteOrder/<str:pk>', views.deleteOrder ,name="delete-order"),
    path('createCustomer/', views.createCustomer_form ,name="create-customer"),
    path('updateCustomer/<str:pk>', views.updateCustomer ,name="update-customer"),
    path('createProduct/', views.createProduct_form ,name="create-product"),
    path('register/', views.register, name="register"),
   ]
