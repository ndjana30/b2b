from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime


# Create your models here.


class Customers(User):
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.username


class Item(models.Model):
    name = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='items/images/')
    posted = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.name


# order
class Purchases(models.Model):
    item = models.ForeignKey(Item, related_name='purchases', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(Customers, related_name='purchased', on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.now())

    @property
    def process(self):
        return self.item.price * self.quantity

    def __str__(self):
        return f'{self.user} purchased {self.item}'


class Deliveries(models.Model):
    items = models.ManyToManyField(Item, related_name='delivery')
    customer = models.ForeignKey(Customers, related_name='deliveries', on_delete=models.CASCADE)

    @property
    def area(self):
        return self.customer.address

    def __str__(self):
        return f'{self.customer} with {self.items}'
