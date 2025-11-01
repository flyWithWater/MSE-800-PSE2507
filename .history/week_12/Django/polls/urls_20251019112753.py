from django.urls import URLPattern, path

from . import hello_world

urlpatterns = [
    path("",hello_world.index,name = "index")
]