from django.urls import path
from .views import index, faq

urlpatterns = [
    path('', index, name="homepage"),
    path('faq/', faq, name='fireapp-faq'),
]

