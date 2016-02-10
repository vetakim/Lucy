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

class RequisitionModel(models.Model):

    arrival_time = models.FloatField()
    start_time = models.FloatField()
    lifetime = models.FloatField()
    duration = models.FloatField()
    action = models.TextField()
    object_type = models.TextField()
    distance = models.FloatField()
    azimuth = models.FloatField()
    row = models.FloatField()
    tact = models.FloatField()
    num = models.IntegerField()
    precedence = models.FloatField()
    catastrophe = models.BooleanField()

    CHOICES = (
            ('arrival_time', 'Arrival time'),
            ('start_time', 'Start time'),
            ('lifetime', 'Lifetime'),
            ('precedence', 'Precedence'),
            ('catastrophe', 'Catastrophe'),
            ('duration', 'Duration'),
            ('action', 'Action'),
            ('object_type', 'Object'),
            ('distance ', 'Distance'),
            ('azimuth', 'Azimuth'),
            ('row', 'Row'),
            ('tact', 'Tact'),
            ('num', 'number'),
            )

