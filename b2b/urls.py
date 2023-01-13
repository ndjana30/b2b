from django.urls import path
from .views import home, _signup_user, login_user, item_details

app_name = 'b2b'

urlpatterns = [
    path('', home, name="home"),
    path('signup/', _signup_user, name="signup"),
    path('login/', login_user, name="login"),
    path('purchase/<int:pk>/<str:name>/', item_details, name="purchase"),

]
