from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class BillType(models.Model):
    name = models.CharField(max_length=20)
    status = models.IntegerField()
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(default=timezone.now)
    

class Bill(models.Model):
    bill_type = models.ForeignKey(BillType,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.FloatField()
    bill_date = models.DateField()
    description = models.CharField(max_length=32,null=True)
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name