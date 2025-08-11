from django.urls import path
from shop.views import base_html,goods_html,users_html

urlpatterns = [
    path('', base_html,name= 'Base'),
    path('goods/',goods_html,name= 'Goods'),
    path('users/',users_html,name= 'Users'),
]