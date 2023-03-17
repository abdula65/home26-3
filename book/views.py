from django.http import HttpResponse
from django.shortcuts import render
from . import models


def hello_word_view(request):
    return HttpResponse("<h1>Hello this is my first Django Project :)</h1>")


def post_view(request):
    post = models.Post.objects.all()
    return render(request, 'index.html', {'post_obj': post})
