from django.db import models


# Create your models here.


class Crypto(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/img")

    def __str__(self):
        return self.name
