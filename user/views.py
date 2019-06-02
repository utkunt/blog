from django.shortcuts import render, redirect, get_object_or_404
from user.forms import RegisterForm, LoginForm, ArticleForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from article.models import Article
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):

	form = RegisterForm(request.POST or None)
	context = {"form":form}

	if form.is_valid():

		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")

		newUser = User(username = username)
		newUser.set_password(password)
		newUser.save()

		login(request, newUser)
		messages.success(request, "Kayıt Alındı ve Giriş Yapıldı")
		return redirect("index")

	return render(request, "register.html", context)

def loginUser(request):

	form = LoginForm(request.POST or None)
	context = {"form":form}

	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")

		user = authenticate(username = username, password = password)

		if user is None:
			messages.warning(request, "Kullanıcı Adı veya Şifre Hatalı")
			return render(request, "login.html", context)

		user.save()
		login(request, user)
		messages.success(request, "Giriş Başarılı")
		return redirect("index")
		
	return render(request, "login.html", context)

@login_required(login_url  = "user:login")
def dashboard(request):

	articles = Article.objects.filter(author = request.user)
	return render(request, "dashboard.html",{"articles":articles})

def logoutUser(request):
	logout(request)
	messages.warning(request, "Çıkış Yapıldı")
	return redirect("index")

@login_required(login_url  = "user:login")
def addarticle(request):

	form = ArticleForm(request.POST or None, request.FILES or None)
	context = {"form":form}

	if form.is_valid():

		article = form.save(commit = False)
		article.author = request.user
		article.save()

		messages.success(request, "Yazı Eklendi")
		return redirect("user:dashboard")
	return render(request, "addarticle.html", context)

def detail(request,id):
	
	#article = Article.objects.filter(id=id).first()
	article = get_object_or_404(Article,id=id)
	return render(request, "detail.html",{"article":article})

@login_required(login_url  = "user:login")
def updateArticle(request,id):

	article = get_object_or_404(Article, id = id)
	form = ArticleForm(request.POST or None, request.FILES or None, instance = article)

	if form.is_valid():
		article = form.save(commit = False)
		article.author = request.user
		article.save()

		messages.success(request, "Yazı Güncellendi")
		return redirect("index")

	return render(request,"update.html",{"form":form})

@login_required(login_url  = "user:login")
def deleteArticle(request, id):

	article = get_object_or_404(Article, id = id)
	article.delete()
	messages.success(request, "Yazı Silindi")
	return redirect("user:dashboard")


