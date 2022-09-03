from django.contrib import admin
from .models import Article,Category,Type

# Register your models here


class ArticleAdmin(admin.ModelAdmin):
#     list_filter = ("article_name","known_for" "born", "died",)
    list_display = ("name","category","type","slug","nationality","known_for","born","died","notable_work","about")
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)
admin.site.register(Type)