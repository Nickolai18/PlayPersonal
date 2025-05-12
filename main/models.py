from django.db import models

# Create your models here.
class Bid(models.Model):
    name = models.CharField((""), max_length=50)
    user = models.CharField((""), max_length=50)

    class Meta:
        verbose_name = ("Заявки")
        verbose_name_plural = ("Заявки")

    def __str__(self):
        return self.name

