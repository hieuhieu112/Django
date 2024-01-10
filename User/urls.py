from django.urls import path
from . import views


app_name = 'user'
urlpatterns = [
    path("login", views.LoginClass.as_view(), name="Index"),
    path("", views.ChatHomeClass.as_view(), name="ChatHome"),
    path("register", views.RegisterClass.as_view(), name="Register"),
    path("create", views.RegisterClass.as_view(),name="Create"),
    path("chat/<int:userID>", views.ChatClass.as_view(), name="ChatDetail"),
    path("search", views.SearchUser.as_view(), name="SearchUser"),
    path("info", views.InforUser.as_view(), name="InfoUser")
]
