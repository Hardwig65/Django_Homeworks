from django.db import models

class ProductDetail(models.Model):
    height =models.FloatField(null=True,blank=True)
    weight =models.FloatField(null=True,blank=True)
    description = models.CharField(max_length=256,blank=True,null=True)

    product = models.OneToOneField(
        to = 'Product',
        on_delete=models.CASCADE,
        related_name = 'product_detail')


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product.name} | {self.description}'