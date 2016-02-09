from django.db import models

class Point(models.Model):
    abscissa = models.FloatField()
    ordinate = models.FloatField()
    noise = models.FloatField()
    CHOICES = (
            ('abscissa', 'Abscissa'),
            ('ordinate', 'Ordinate'),
            ('noise', 'Noise')
            )

# Create your models here.

class Requisitions(models.Model):

    arrival_time = models.FloatField()
    lifetime = models.FloatField()
    duration = models.FloatField()
    action = models.TextField()
    object_type = models.TextField()
    distance = models.FloatField()
    azimuth = models.FloatField()
    row = models.FloatField()
    tact = models.FloatField()

    CHOICES = (
            ('arrival_time', 'Arrival time'),
            ('lifetime', 'Lifetime'),
            ('duration', 'Duration'),
            ('action', 'Action'),
            ('object_type', 'Object'),
            ('distance ', 'Distance'),
            ('azimuth', 'Azimuth'),
            ('row', 'Row'),
            ('tact', 'Tact'),
            )

