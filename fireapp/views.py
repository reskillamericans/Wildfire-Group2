from django.contrib.messages.api import success
from django.contrib.messages.constants import SUCCESS
from django.core.checks import messages
from django.conf import settings
from django.shortcuts import redirect, render
from .models import Newsletter, Faq
from django.contrib.auth.models import User
from .forms import NewsletterForm
from django.core.mail import send_mail
from django.contrib import messages
from .helper import newsletter



# Newsletter view
def index(request):
    template_name = "fireapp/index.html"

    if newsletter(request):
        return redirect("homepage")

    context = {"newsletter_form": NewsletterForm()}
    return render(request, template_name, context)



# About Us
def about_us(request):
    template_name = "fireapp/about-us.html"

    if newsletter(request):
        return redirect("homepage")

    context = {"newsletter_form": NewsletterForm()}
    return render(request, template_name, context)


# Frequently Asked Questions
def faq(request):
    if newsletter(request):
        return redirect("homepage")

    context = {
        'questions' : Faq.objects.all(),
        'newsletter_form': NewsletterForm()
    }
    return render(request, 'fireapp/faq.html', context)
