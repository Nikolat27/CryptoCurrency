from django.db import models


# Create your models here.


class Crypto(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50)
    image = models.ImageField(upload_to="img")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = self.name.lower()
        self.symbol = self.symbol.lower()

    def __str__(self):
        return self.name
