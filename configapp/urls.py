
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('create_contract/', views.create_contract, name='create_contract'),
    path('contracts_detail/<int:pk>/', views.contract_detail, name='contract_detail'),
    path('contracts_list/', views.contracts_list, name='contracts_list'),
    path('drivers_list/', views.drivers_list, name='drivers_list'),
    path('add_driver/', views.add_driver, name='add_driver'),
    path('users_list/', views.users_list, name='users_list'),
    path('add_user/', views.add_user, name='add_user'),
    path('cars_list/', views.cars_list, name='cars_list'),
    path('add_car/', views.add_car, name='add_car'),
    path('contracts/',views.contracts_list,name = 'contracts_list')
]
