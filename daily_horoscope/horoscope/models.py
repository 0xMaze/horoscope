from django.db import models

# Create your models here.


class Horoscope(models.Model):
    sign = models.CharField(max_length=20)
    date = models.DateField()
    horoscope = models.TextField()

    def __str__(self):
        return self.sign
