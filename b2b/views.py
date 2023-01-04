from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'b2b/home/home.html')
