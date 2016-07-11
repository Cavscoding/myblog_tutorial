from django.contrib import admin
from article.models import Article

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'date_time')
	list_filter = ('category', 'date_time')
	search_fields = ['title']


admin.site.register(Article, ArticleAdmin)