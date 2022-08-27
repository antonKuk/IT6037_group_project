from pickle import TRUE
from django.db import models
from django.core.validators import MinLengthValidator

'''Article Model'''

class Articles(models.Model):
    slug = models.SlugField(unique=True, db_index=True)
    article_name = models.CharField(max_length=150)
    about = models.TextField(validators=[MinLengthValidator(10)])
#     image = models.ImageField(upload_to="posts", null=True)
    date_born = models.DateField()
    date_died = models.DateField()
    nationality = models.CharField(max_length=150)
    known_for = models.CharField(max_length=255)
    notable_work =models.CharField(max_length=255)

    def __str__(self):
        return self.article_name