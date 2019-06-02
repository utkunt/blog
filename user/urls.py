from django.contrib import admin
from django.urls import path
from user.views import *

app_name = "user"

urlpatterns = [
	path("register/", register, name = "register"),
	path("login/", loginUser, name = "login"),
	path("dashboard/", dashboard, name = "dashboard"),
	path("logout/", logoutUser, name = "logout"),
	path("addarticle/", addarticle, name = "addarticle"),
	path("detail/<int:id>", detail, name = "detail"),
	path("update/<int:id>", updateArticle, name = "update"),
	path("delete/<int:id>", deleteArticle, name = "delete")
]