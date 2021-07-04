from django.urls import path
from .views import news_letter_view

urlpatterns = [
    path('newsletter/', news_letter_view, name="news-letter"),
]

