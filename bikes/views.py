from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'bikes/index.html')

def contact(request):
    return render(request, 'bikes/contact.html')

def about(request):
    return render(request, 'bikes/about.html')

def login(request):
    return render(request, 'bikes/login.html')

def shopsingle(request):
    return render(request, 'bikes/shop-single.html')

def shop(request):
    return render(request, 'bikes/shop.html')

