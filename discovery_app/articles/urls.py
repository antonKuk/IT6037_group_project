
from django.urls import path
from .views import CreateArticleView
from . import views
# from articles import views


urlpatterns = [
    path("",views.HomePageView.as_view(), name="home-page"),
    path("article/new/",CreateArticleView.as_view(),name="article-create")

] 
