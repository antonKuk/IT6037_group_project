from django.contrib import admin
from .models import Articles

# Register your models here


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ("name","nationality","known_for","born","died","notable_work","about","category","type","dimensions","location","medium","designed_by","developer")

admin.site.register(Articles,ArticlesAdmin)