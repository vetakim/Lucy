from django.db import models

class Point(models.Model):
    abscissa = models.FloatField()
    ordinate = models.FloatField()
    noise = models.FloatField()


# Create your models here.
