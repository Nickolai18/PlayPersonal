from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Games(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=300)
    link = models.URLField(max_length=100)
    image = models.ImageField()
    isActive = models.BooleanField(default=False)
    


    class Meta:
        verbose_name = ("Игры")
        verbose_name_plural = ("Игры")

    def __str__(self):
        return self.name
class Bid(models.Model):
    name = models.CharField((""), max_length=50)
    user = models.CharField((""), max_length=50)

    class Meta:
        verbose_name = ("Заявки")
        verbose_name_plural = ("Заявки")

    def __str__(self):
        return self.name

