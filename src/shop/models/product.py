from django.utils.translation import gettext_lazy as _
from django.db import models


class ProductCategory(models.TextChoices):
    TECH = 'TQ', _("Technique")
    BOOK = 'BK', _("Book")
    FURNITURE = 'FR', _("Furniture")
    SPORT = 'SP', _("Sport")
    CHILDREN = 'CN', _("Children")
    DEFAULT = 'DF', _("Default")

class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name=_("Имя продукта"))
    description = models.CharField(max_length=200, null=True,blank=True, verbose_name=_('Описание'))
    price = models.FloatField(verbose_name='Цена')
    is_available = models.BooleanField(default=True,verbose_name='Наличие')
    category = models.CharField(choices=ProductCategory,
                                default=ProductCategory.DEFAULT, verbose_name='Категория')
    rating = models.FloatField(null=True,blank=True,verbose_name='Рейтинг')
    photo = models.ImageField(null=True,blank=True,verbose_name='Фото')
    count_items = models.IntegerField(default=10,verbose_name='Количество')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    provider = models.ForeignKey(to = 'Provider',
                                 on_delete=models.SET_NULL,
                                 related_name='products',
                                 blank = True,
                                 null=True)



    def __str__(self):
        return f'{self.name} | {self.price}$'

