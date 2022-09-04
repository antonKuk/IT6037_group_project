from django.urls import path
from .views import CreateArticleView
from . import views
# from articles import views


urlpatterns = [
    path("",views.HomePageView.as_view(), name="home-page"),
    path("articles/new/",CreateArticleView.as_view(),name="article-create"),
    path("articles/<slug:slug>",views.DetailArticlelView.as_view(),name="detail-page"),
    path("articles/<slug:slug>/update/",views.UpdateArticleView.as_view(),name="update-page"),
    path("articles/<slug:slug>/delete/",views.DeleteArticleView.as_view(),name="delete-page"),
]