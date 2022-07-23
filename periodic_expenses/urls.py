from django.urls import path
from . import views

urlpatterns = [
    path("", views.Periodic.as_view(), name="periodic"),
]
