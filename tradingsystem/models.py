from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver

class Stock(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=7, decimal_places=2)

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    stocks = models.ForeignKey(Stock,on_delete=models.CASCADE,default=None,null=True)
    qty = models.DecimalField(max_digits=7,decimal_places=0)
