from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Item)
admin.site.register(Purchases)
admin.site.register(Deliveries)
admin.site.register(Customers)
