from django.urls import URLPattern, path,include
from django.contrib import admin

from . import views

urlpatterns = [
    path("/",views.index,name = "index"),

]