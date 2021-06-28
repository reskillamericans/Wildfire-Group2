from django.urls import path
from .views import NewsletterView, faq

urlpatterns = [
    path('newsletter/', NewsletterView.as_view(), name="news-letter"),
    # path('faq/', faq, name='fireapp-faq'),
]

