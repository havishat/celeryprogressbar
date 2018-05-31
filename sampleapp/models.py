from __future__ import absolute_import, unicode_literals
from django.db import models

# Create your models here.
class Calcu(models.Model):
    n = models.CharField(max_length=10)