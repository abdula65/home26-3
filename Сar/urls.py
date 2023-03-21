from django.urls import path
from . import views

urlpatterns = [
    path('Сar_list/', views.Сar_list_view, name='Сar_list'),
    path('Сar_list/<int:id>/', views.Сar_detail_view, name='Сar_detail'),
]