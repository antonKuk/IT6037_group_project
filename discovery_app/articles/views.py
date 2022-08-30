from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView,DetailView,CreateView
from .models import Articles
from .article_form import ArticleForm





# Create your views here.

# def home(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

class HomePageView(ListView):
    template_name = "articles/home.html"
    model = Articles
    # ordering = ["-date"]
    context_object_name = "articles"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:5]
        return data


# class CreateArticleView(CreateView):
#      model= Articles
#      fields=['article_name','about','date_born','date_died','nationality','known_for',"notable_work"]   


class CreateArticleView(CreateView):

    def get(self, request,):
        context = {
          "article_form": ArticleForm(),
        }
        return render(request, "articles/article-create.html", context)

    def post(self, request):
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
          article = article_form.save(commit=False)
          article.save()
          return HttpResponseRedirect(reverse("home-page"))

        context = {
          "article_form": article_form,
        }
        return render(request, "articles/article-create.html", context)   



    # def save(self, *args, **kwargs):
    #         self.slug = slugify(self.title)
    #         super(Articles, self).save(*args, **kwargs)

     # class Meta:
     #      model= Articles
     #      fields=['article_name','about','date_born','date_died','nationality','known_for',"notable_work"]        