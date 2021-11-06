from django.urls import path

from . import views


urlpatterns = [
    path("", views.ModelsView.as_view()),
]