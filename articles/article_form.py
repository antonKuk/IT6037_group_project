
from django import forms
from django.utils.text import slugify
from .models import Article

''' Comment Form'''

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # fields = '__all__'
        # # field_classes = {'slug': slugify(field="article_name"),}
        exclude = ["slug"]
        labels = {
          "article_name": "article name",
          "slug": "slug",
          "nationality": "nationality",
          "date_born": "date born",
          "date_died": "date died",
          "known_for": "known for",
          "notable_work": "notable work",
          "about": "type about the article here...",
        }
