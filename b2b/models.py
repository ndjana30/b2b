from django.contrib.auth.models import User
from django.db import models
import datetime


# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='items/images/')
    posted = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.name


class Purchase(models.Model):
    item = models.ForeignKey(Items, related_name='purchases', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, related_name='purchased', on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.now())

    @property
    def process(self):
        return self.item.price * self.quantity

    def __str__(self):
        return f'{self.user} purchased {self.item} for'
