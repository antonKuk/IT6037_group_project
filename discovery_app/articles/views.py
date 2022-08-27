from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView,DetailView
from .models import Articles



# Create your views here.

def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# class HomePageView(ListView):
#     template_name = "home.html"
#     model = Articles
