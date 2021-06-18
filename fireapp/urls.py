from django.urls import path
from .views import NewsletterView

urlpatterns = [
    path('newsletter/', NewsletterView.as_view(), name="news-letter"),
]

