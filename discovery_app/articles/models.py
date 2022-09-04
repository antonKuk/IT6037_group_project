from django.utils.text import slugify
from pickle import TRUE
from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse

'''Article Model'''

CATEGORY_LIST = [
    ('', 'Choose...'),
    ('Arts', 'Arts'),
    ('Mathematics', 'Mathematics'),
    ('Technology', 'Technology'),
]

TYPE_LIST = [
    ('', 'Choose...'),
    ('Algorithm', 'Algorithm'),
    ('Biography', 'Biography'),
    ('Painting', 'Painting'),
    ('Programming Language', 'Programming Language'),
    ('Theorem', 'Theorem'),
]

class Category(models.Model):
    category_name=models.CharField(max_length=150, choices=CATEGORY_LIST, default='Choose...')

    def __str__(self):
        return self.category_name

class Type(models.Model):
    type_name=models.CharField(max_length=150, choices=TYPE_LIST, default='Choose...')

    def __str__(self):
        return self.type_name

class Article(models.Model):
    slug = models.SlugField(unique=True, db_index=True)
    name = models.CharField(max_length=150)
    designed_by = models.CharField(max_length=150, blank=True)
    developer = models.CharField(max_length=150, blank=True)
    dimensions = models.CharField(max_length=40, blank=True)
    about = models.TextField(validators=[MinLengthValidator(10)])
    image = models.ImageField(upload_to='images/', null=True, blank=True, default='Null')
    born = models.DateField(blank=True)
    died = models.DateField(blank=True)
    nationality = models.CharField(max_length=150, blank=True)
    known_for = models.CharField(max_length=255, blank=True)
    notable_work = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=100, blank=True)
    medium = models.CharField(max_length=150, blank=True)
    year = models.DateField(null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="category")
    type = models.ForeignKey(
        Type, on_delete=models.SET_NULL, null=True, related_name="type")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home-page")
        
    def save(self, *args, **kwargs):
            self.slug = slugify(self.name)
            super(Article,self).save(*args, **kwargs)