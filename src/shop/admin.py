from django.contrib import admin
from shop.models import (
    Order,
    Feedback,
    ProductDetail,
    Provider,
    ProductOrder
)

# Register your models here.
admin.site.register(Order)
admin.site.register(Feedback)
admin.site.register(ProductDetail)
admin.site.register(Provider)
admin.site.register(ProductOrder)