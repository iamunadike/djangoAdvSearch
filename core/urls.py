from django.urls import path
from .views import SimpleForm
urlpatterns = [
     path("form", SimpleForm, name="form"),
]
