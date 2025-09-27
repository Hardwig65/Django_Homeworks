from django.db import models
from django.conf import settings
from shop.models.base import TimeConfig


class Feedback(TimeConfig):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=256, null=True, blank=True)

    products = models.ForeignKey(to = 'Product',
                                on_delete=models.CASCADE,
                                related_name='feedbacks',
                                null=True,
                                blank=True)

    User = models.ForeignKey(to = settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='feedbacks',
                             blank=True,
                             null=True)


    def __str__(self):
        return f'{self.title} | {self.products.name}'