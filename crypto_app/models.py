from django.db import models


# Create your models here.


class Crypto(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50)
    image = models.ImageField(upload_to="img")

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.name = self.name.lower()
        self.symbol = self.symbol.lower()
        super(Crypto, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
