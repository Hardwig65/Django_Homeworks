
from shop.models.base import Rating,TimeConfig
from django.db import models

class UserRating(Rating, TimeConfig):
    user = models.ForeignKey(
        to = 'CustomUser',
        related_name = 'user_rating',
        on_delete=models.SET_NULL,
        null = True,
        blank = True,)


    user_detail = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.title