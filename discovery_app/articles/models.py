from django.utils.text import slugify
from pickle import TRUE
from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator
from django.urls import reverse

'''Article Model'''

# class Articles(models.Model):
#     slug = models.SlugField(unique=True, db_index=True,null=True)
#     article_name = models.CharField(max_length=150)
#     about = models.TextField(validators=[MinLengthValidator(10)])

#     date_born = models.DateField()
#     date_died = models.DateField()
#     nationality = models.CharField(max_length=150)
#     known_for = models.CharField(max_length=255)
#     notable_work =models.CharField(max_length=255)

#     def __str__(self):
#         return self.article_name

#     def get_absolute_url(self):
#         return reverse("home-page")


#     def save(self, *args, **kwargs):
#             self.slug = slugify(self.article_name)
#             super(Articles,self).save(*args, **kwargs)


class Category(models.Model):
    category_name = models.CharField(max_length=150)

    def __str__(self):
        return self.category_name


class Type(models.Model):
    type_name = models.CharField(max_length=150)

    def __str__(self):
        return self.type_name


class Article(models.Model):
    slug = models.SlugField(unique=True, db_index=True)
    article_name = models.CharField(max_length=150)
    designed_by = models.CharField(max_length=150, blank=True)
    developer = models.CharField(max_length=150, blank=True)
    dimensions = models.CharField(max_length=40, blank=True)
    about = models.TextField(validators=[MinLengthValidator(10)])
#     image = models.ImageField(upload_to="posts", null=True)
    # date_born = models.DateField(blank=True)
    # date_died = models.DateField(blank=True)
    date_born = models.CharField(max_length=40, blank=True)
    date_died = models.CharField(max_length=40, blank=True)

    nationality = models.CharField(max_length=150, blank=True)
    known_for = models.CharField(max_length=255, blank=True)
    notable_work = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=100, blank=True)
    medium = models.CharField(max_length=150, blank=True)
    # year = models.DateField(null=True)
    year = models.CharField(max_length=40, blank=True)

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="category")
    type = models.ForeignKey(
        Type, on_delete=models.SET_NULL, null=True, related_name="type")

    def __str__(self):
        return self.article_name

    def get_absolute_url(self):
        return reverse("home-page")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.article_name)
        super(Article, self).save(*args, **kwargs)
