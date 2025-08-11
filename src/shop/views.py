from django.shortcuts import render
from django.http import HttpResponse

def base_html(request):
    return render(request,'base.html')
def goods_html(request):
    goods = [
        {"good_name": "Toy Car", "status": "available", "category": "children"},
        {"good_name": "Laptop", "status": "out of stock", "category": "electronics"},
        {"good_name": "T-shirt", "status": "available", "category": "clothing"},
        {"good_name": "Book - Python Basics", "status": "available", "category": "books"},
        {"good_name": "Board Game", "status": "available", "category": "children"},
    ]
    context = {
        'goods': goods,
    }
    return render(request,'goods.html',context)
def users_html(request):
    users = [
        {"name": "John Smith", "age": 28, "phone": "+1-202-555-0123"},
        {"name": "Anna Johnson", "age": 34, "phone": "+1-202-555-0456"},
        {"name": "Mark Davis", "age": 22, "phone": "+1-202-555-0789"},
        {"name": "Emily White", "age": 19, "phone": "+1-202-555-0999"},
        {"name": "David Brown", "age": 40, "phone": "+1-202-555-0666"},
    ]
    context = {
        'users': users,
    }
    return render(request,'users.html',context)