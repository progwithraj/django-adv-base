from django.urls import path
from .views import indexView

app_name = 'subCore'
urlpatterns = [
    path('', indexView, name='index'),
]