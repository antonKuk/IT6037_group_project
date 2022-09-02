from importlib.util import module_for_loader
from pickle import TRUE
from django.db import models
from django.core.validators import MinLengthValidator

'''Article Model'''


class Articles(models.Model):
    slug = models.SlugField(unique=True, db_index=True)
    article_name = models.CharField(max_length=150)
    category = models.CharField(max_length=50)
    designed_by = models.CharField(max_length=150)
    developer = models.CharField(max_length=150)
    dimensions = models.CharField(max_length=40)
    about = models.TextField(validators=[MinLengthValidator(10)])
#     image = models.ImageField(upload_to="posts", null=True)
    date_born = models.DateField()
    date_died = models.DateField()
    nationality = models.CharField(max_length=150)
    known_for = models.CharField(max_length=255)
    notable_work = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    medium = models.CharField(max_length=150)
    type = models.CharField(max_length=100)
    year = models.DateField()

    def __str__(self):
        return self.article_name
