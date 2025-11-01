from django.urls import URLPattern, path,include

from . import hello_world

urlpatterns = [
    path("",hello_world.index,name = "index"),
    path("polls",include("polls.urls")),
    path("admin",admin.site.urls)
]