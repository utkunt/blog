from django.shortcuts import render
from article.models import Article

# Create your views here.
def index(request):
	return render(request, "index.html")

def about(request):
	return render(request, "about.html")

def article(request):

	keyword = request.GET.get("keyword")

	if keyword:
		articles = Article.objects.filter(title__contains = keyword)
		return render(request, "article.html",{"articles":articles})

	articles = Article.objects.all()
	return render(request, "article.html",{"articles":articles})
