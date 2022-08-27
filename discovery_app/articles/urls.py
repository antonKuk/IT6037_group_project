
from django.urls import path
from . import views
# from articles import views


urlpatterns = [
    path("",views.HomePageView.as_view(), name="home-page"),
] 
