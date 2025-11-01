from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
 


def index(request):
    return render(request,'polls/templates/hello_world.html')