from django.contrib import admin
from article.models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'date_time')
	list_filter = ('category', 'date_time')
	search_fields = ['title']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)