from django.urls import path
from .views import newsletter, faq

urlpatterns = [
    path('newsletter/', newsletter, name="news-letter"),
    #path('faq/', faq, name='fireapp-faq'),
]

