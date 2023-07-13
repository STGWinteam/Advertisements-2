from .views import index
from django.urls import path

urlpatterns: list[path] = [
    path("lesson_4", index)
]