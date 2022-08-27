from django.contrib import admin
from .models import Articles

# Register your models here


class ArticlesAdmin(admin.ModelAdmin):
#     list_filter = ("article_name","known_for" "born", "died",)
    list_display = ("article_name","slug","nationality","known_for","date_born","date_died","notable_work","about")
    prepopulated_fields = {"slug": ("article_name",)}


admin.site.register(Articles,ArticlesAdmin)
