from django.urls import path
from .views import index, faq, about_us, contact

urlpatterns = [
    path('', index, name="homepage"),
    path('faq/', faq, name='faq'),
    path('about-us/', about_us, name="about_us"),
    path('contact/', contact, name="contact"),
]