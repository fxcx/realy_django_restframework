from django.urls import path
from .views import reder_article

urlpatterns = [
    path('', reder_article, name='articles' ),
]
