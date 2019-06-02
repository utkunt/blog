from django.contrib import admin
from article.models import Article


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

	list_display = ["title", "author", "date"]
	list_display_links = ["title"]
	list_filter = ["date"]
	search_fields =["title"]

	class Meta:

		model = Article