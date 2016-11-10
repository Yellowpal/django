from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Bill(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    bill_date = models.DateField()
    create_date = models.DateTimeField(default=timezone.now)