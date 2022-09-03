from django.contrib import admin
from .models import Article,Category,Type

# Register your models here


class ArticleAdmin(admin.ModelAdmin):
#     list_filter = ("article_name","known_for" "born", "died",)
    list_display = ("article_name","category","type","slug","nationality","known_for","date_born","date_died","notable_work","about")
    prepopulated_fields = {"slug": ("article_name",)}


admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)
admin.site.register(Type)