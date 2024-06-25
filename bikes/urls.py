from django.urls import path
from .views import index, about, contact, login, shopsingle, shop

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('shopsingle/', shopsingle, name='shopsingle'),
    path('shop/', shop, name='shop'),
]