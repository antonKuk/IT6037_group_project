from importlib.util import module_for_loader
from pickle import TRUE
from django.db import models
from django.core.validators import MinLengthValidator

'''Article Model'''


class Articles(models.Model):
    slug = models.SlugField(unique=True, db_index=True)
    article_name = models.CharField(max_length=150)
    lecture_category = models.CharField(max_length=50, blank=True)
    designed_by = models.CharField(max_length=150, blank=True)
    developer = models.CharField(max_length=150, blank=True)
    dimensions = models.CharField(max_length=40, blank=True)
    about = models.TextField(validators=[MinLengthValidator(10)])
#     image = models.ImageField(upload_to="posts", null=True)
    date_born = models.DateField(blank=True)
    date_died = models.DateField(blank=True)
    nationality = models.CharField(max_length=150, blank=True)
    known_for = models.CharField(max_length=255, blank=True)
    notable_work = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=100, blank=True)
    medium = models.CharField(max_length=150, blank=True)
    type = models.CharField(max_length=100, blank=True)
    year = models.DateField(null=True)

    def __str__(self):
        return self.article_name
