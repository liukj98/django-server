from django.urls import path

from . import views

urlpatterns = [
    path("keygeneration", views.keyGeneration, name="keyGeneration"),
]