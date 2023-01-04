from django.urls import path
from .views import home

app_name = 'b2b'

urlpatterns = [
    path('', home, name="home"),
]
