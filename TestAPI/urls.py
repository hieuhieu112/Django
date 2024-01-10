from django.urls import path
from . import views


app_name = 'api'
urlpatterns = [
    path("", views.GetAllCourseAPI.as_view(), name="api")
    ]