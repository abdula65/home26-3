from django.urls import path
from . import views

urlpatterns = [
    path('Сar_list/', views.Сar_list_view, name='Сar_list'),
    path('Сar_list/<int:id>/', views.Сar_detail_view, name='Сar_detail'),
    path('car_list/<int:id>/delete/', views.delete_car_view, name='delete'),
    path('car_list/<int:id>/update/', views.update_car_view, name='update'),
    path('create_car/', views.create_car_view, name='create'),
    path('car_list/<int:id>/reviews/', views.reviews_car_view, name='reviews'),
]