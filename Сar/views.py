from django.shortcuts import render, get_object_or_404
from . import models


# не полная информация о товаре
def Сar_list_view(request):
    Сar_object = models.Cars.objects.all()
    return render(request, 'Сar_list.html', {'Сar_object': Сar_object})


# Полная информация об объекте по id
def Сar_detail_view(request, id):
    Сar_detail = get_object_or_404(models.Cars, id=id)
    return render(request, 'Сar_detail.html', {'Сar_detail': Сar_detail})
