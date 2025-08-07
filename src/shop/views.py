from django.shortcuts import render
from django.http import HttpResponse

def shop_info(request):
    return HttpResponse("<h1>Интернет-магазин</h1>")

def shop_page(request):
    return HttpResponse("<h1>Эта страница нужна для товаров</h1>")
