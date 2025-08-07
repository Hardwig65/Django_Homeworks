from django.urls import path
from shop.views import shop_info,shop_page

urlpatterns = [
    path('info/',shop_info),
    path('page/', shop_page),
]