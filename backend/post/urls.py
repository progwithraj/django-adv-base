from .views import index
from django.urls import path

app_name = "post"

urlpatterns = [
    path("", index, name="index"),
]
