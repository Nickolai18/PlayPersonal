from django.db import models

class Bid(models.Model):
    name = models.CharField("", max_length=50)
    user = models.CharField("", max_length=50)
    status = models.CharField("", max_length=20, default='pending')
    rating = models.IntegerField("", default=0)

    class Meta:
        verbose_name = "Заявки"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return self.name

class Comment(models.Model):
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE, related_name='comments')
    user = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
