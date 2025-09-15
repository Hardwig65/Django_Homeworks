from django.contrib import admin
from shop.models import (
    Product,
    Order,
    Feedback,
    ProductDetail,
    Provider,
    ProductOrder
)

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Feedback)
admin.site.register(ProductDetail)
admin.site.register(Provider)
admin.site.register(ProductOrder)