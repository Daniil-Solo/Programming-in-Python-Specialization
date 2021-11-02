from django.db import models


class Jewelry(models.Model):
    title = models.CharField(max_length=64)
    price = models.FloatField()
    photo = models.ImageField(upload_to='photo/jewelry')
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
