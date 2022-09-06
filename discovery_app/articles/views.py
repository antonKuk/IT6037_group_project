from django.urls import reverse
from django.shortcuts import render
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Article
from .article_form import ArticleForm





# Create your views here.

# def home(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
# class SearchResultsView(ListView):
#     model =  Article
#     template_name = '/search_results.html'

#     def get_queryset(self): # new
#         query = self.request.GET.get("q")
#         object_list = Arcicle.objects.filter(
#             Q(title__icontains=query)
#         )
#         return object_list


class HomePageView(ListView):
    template_name = "articles/home.html"
    model = Article
    # ordering = ["-date"]
    context_object_name = "articles"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:20]
        return data

class DetailArticlelView(LoginRequiredMixin, DetailView):
    model = Article
    template_name="articles/article-detail.html"
    form_class = ArticleForm
    context_object_name="articles"
    # queryset=Articles.objects.all()

    # def get_object(self):
    #   slug=self.kwargs.get("slug")
    #   return get_object_or_404(Articles,slug=slug)

    # def form_valid(self,form):
    #   print(form.cleaned_data)
    #   return super().form_valid(form)

class CreateArticleView(LoginRequiredMixin, CreateView):

    def get(self, request):
        context = {
          "article_form": ArticleForm(),
           "title":"Create Article",
           "action":"Create",
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



class UpdateArticleView(LoginRequiredMixin, UpdateView):
    template_name="articles/article-update.html"
    form_class = ArticleForm
    queryset=Article.objects.all()

    def get_object(self):
      slug=self.kwargs.get("slug")
      return get_object_or_404(Article,slug=slug)

    def form_valid(self,form):
      return super().form_valid(form)


class DeleteArticleView(LoginRequiredMixin, DeleteView):
    template_name="articles/article-delete.html"
    model=ArticleForm
    success_url='/'

    def get_object(self):
      slug=self.kwargs.get("slug")
      return get_object_or_404(Article,slug=slug)

    # def test_func(self):
    #   article=self.get_object()
 


