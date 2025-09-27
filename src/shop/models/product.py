from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models
from shop.models.base import TimeConfig


class ProductCategory(models.TextChoices):
    TECH = 'TQ', _("Technique")
    BOOK = 'BK', _("Book")
    FURNITURE = 'FR', _("Furniture")
    SPORT = 'SP', _("Sport")
    CHILDREN = 'CN', _("Children")
    DEFAULT = 'DF', _("Default")

class Product(TimeConfig):
    name = models.CharField(max_length=30, verbose_name=_("Имя продукта"))
    description = models.CharField(max_length=200, null=True,blank=True, verbose_name=_('Описание'))
    price = models.FloatField(verbose_name='Цена')
    is_available = models.BooleanField(default=True,verbose_name='Наличие')
    category = models.CharField(choices=ProductCategory,
                                default=ProductCategory.DEFAULT, verbose_name='Категория')
    photo = models.ImageField(null=True,blank=True,verbose_name='Фото')
    count_items = models.IntegerField(default=10,verbose_name='Количество')


    def clean(self):
        super().clean()
        if self.price is not None and self.price <= 0:
            raise ValidationError({'price':'Цена должна быть больше 0.'})

    provider = models.ForeignKey(to = 'Provider',
                                 on_delete=models.SET_NULL,
                                 related_name='products',
                                 blank = True,
                                 null=True)




    def __str__(self):
        return f'{self.name} | {self.price}$'

