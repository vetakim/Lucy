from django.db import models

class Point(models.Model):
    abscissa = models.FloatField()
    ordinate = models.FloatField()
    noise = models.FloatField()
    CHOICES = (
            (abscissa, 'Abscissa'),
            (ordinate, 'Ordinate'),
            (noise, 'Noise')
            )


# Create your models here.
