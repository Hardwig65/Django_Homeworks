from django.db import models
from shop.models.base import TimeConfig


class ProductDetail(TimeConfig):
    height =models.FloatField(null=True,blank=True)
    weight =models.FloatField(null=True,blank=True)
    description = models.CharField(max_length=256,blank=True,null=True)

    product = models.OneToOneField(
        to = 'Product',
        on_delete=models.CASCADE,
        related_name = 'product_detail')




    def __str__(self):
        return f'{self.product.name} | {self.description}'