from django.db import models

class TimeConfig(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Rating(TimeConfig):
    stars = models.FloatField()
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.title
