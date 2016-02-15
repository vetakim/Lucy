from django.db import models
from priority.scheduler import laws

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

class RequisitionInput(models.Model):
    IN_CHOICES = tuple((j, j) for j in laws)
    maxtact = models.FloatField()
    free_resource = models.FloatField()
    medium = models.FloatField()
    dispersion = models.FloatField()
    lawstring = models.CharField(max_length=255,
            choices = IN_CHOICES,
            default = IN_CHOICES[0][0])

class RequisitionOutput(models.Model):
    arrival_time = models.FloatField()
    start_time = models.FloatField()
    lifetime = models.FloatField()
    duration = models.FloatField()
    action = models.CharField(max_length=255)
    object_type = models.CharField(max_length=255)
    distance = models.FloatField()
    azimuth = models.FloatField()
    row = models.FloatField()
    tact = models.FloatField()
    num = models.IntegerField()
    numinbarrier = models.IntegerField()
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
            ('distance', 'Distance'),
            ('azimuth', 'Azimuth'),
            ('row', 'Row'),
            ('tact', 'Tact'),
            ('num', 'number'),
            ('numinbarrier', 'numinbarrier'),
            )

