from django.urls import path

from .views import index

app_name = "post"

urlpatterns = [
    path("", index, name="index"),
]
