from django.db import models

# Create your models here.


class Families(models.Model):
    name = models.CharField(max_length=40)
    age = models.FloatField()
    sex = models.BooleanField()