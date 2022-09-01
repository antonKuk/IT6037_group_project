
from django.urls import path
from .views import CreateArticleView
from . import views
# from articles import views


urlpatterns = [
    path("",views.HomePageView.as_view(), name="home-page"),
    path("article/new/",CreateArticleView.as_view(),name="article-create"),
    path("article/<slug:slug>",views.DetailArticlelView.as_view(),name="detail-page"),
    path("article/<slug:slug>/update/",views.UpdateArticleView.as_view(),name="update-page"),
    path("article/<slug:slug>/delete/",views.DeleteArticleView.as_view(),name="delete-page"),



] 
