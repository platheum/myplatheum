from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import home, success, suscribe


urlpatterns = [

    path('', home),
    path('success/', success),
    path('suscribe/', suscribe),
]