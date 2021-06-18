from django.contrib.messages.api import success
from django.contrib.messages.constants import SUCCESS
from django.http import HttpResponse, request
from .models import Newsletter
from django.views.generic import CreateView


# Create your views here.
def index(request):
    return HttpResponse("<h1>Wildfire App 2</h1>")


class NewsletterView(CreateView):
    template_name = 'newsletter/newsletter.html'
    model = Newsletter
    fields = ['email',]
    success_message = "your email has been added to our newsletter list"


