from unicodedata import category
import django_filters
from django_filters import CharFilter, ChoiceFilter

from .models import *


    
class ArticleFilter(django_filters.FilterSet):


	title = CharFilter(field_name='article_name', lookup_expr='icontains', label='Search by Title')
	# category = ChoiceFilter(field_name='category', choices='STATUS_CHOICES ', default=0)





	class Meta:
		model = Article
		fields = ['category']
		#exclude = ['slug', 'designed_by' , 'developer']