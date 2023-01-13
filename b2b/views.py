from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Customers, Purchases, Item, Deliveries
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.
@login_required
def home(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'b2b/home/home.html', context)


@login_required
def item_details(request, pk, name):
    item = Item.objects.get(pk=pk, name=name)
    if request.method == 'POST':
        q = request.POST.get('quantity')
        quantity = int(q)
        user = request.user
        customer = Customers.objects.get(username=user)
        if customer is not None:
            if customer.is_active:
                item = item
                pur = Purchases(user=customer, item=item, quantity=quantity)
                pur.save()
                total = pur.process
                messages.success(request, f"Purchase successful with amount {total}")
    context = {'item': item}
    return render(request, 'b2b/purchase/item-details.html', context)


def _signup_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            customer = Customers.objects.create_user(username, email, password1)
            customer.first_name = first_name
            customer.last_name = last_name
            customer.address = address
            customer.phone = phone
            customer.save()
            messages.success(request, "Account creation successful")
            login(request, customer)
            return redirect("b2b:home")
        else:
            messages.error(request, "Passwords not matching")
    return render(request, 'b2b/signup/signup.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'login successful')
        except user.DoesNotExist:
            messages.error(request, 'wrong credentials')
    return render(request, 'b2b/login/login.html')
