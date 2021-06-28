from django.contrib.messages.api import success
from django.contrib.messages.constants import SUCCESS
from django.core.checks import messages
from django.http import request
from django.shortcuts import HttpResponse, get_object_or_404, render
from .models import Newsletter, Faq
from django.views.generic import CreateView
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.
def index(request):
    return HttpResponse("<h1>Wildfire App 2</h1>")


class NewsletterView(CreateView):
    template_name = 'newsletter/newsletter.html'
    model = Newsletter
    fields = ['email',]

    def form_valid(self, form):
        send_mail(
            subject="Welcome to Reskill wildfire Subscription",
            message="You have subscribed to Reskill Americans wildfire subscription",
            from_email="liomes8016@gmail.com",
            recipient_list=[str(form.instance.email)],
            fail_silently=False
        )
        messages.success(self.request, f"your email {form.instance.email} has been added to our newsletter successfully")
        return super().form_valid(form)

def faq(request):

    context = {
        'questions' : Faq.objects.all() 
    }

    return render(request, 'fireapp/faq.html', context)