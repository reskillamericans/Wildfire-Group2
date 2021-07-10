from django.contrib.messages.api import success
from django.contrib.messages.constants import SUCCESS
from django.core.checks import messages
from django.conf import settings
from django.shortcuts import redirect, render
from .models import Faq
from django.contrib.auth.models import User
from .forms import NewsletterForm, SubmitQuestion
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

# Contact Us
def contact(request):
    if request.method == 'POST':
        if request.POST.__contains__('full_name'):
            contact_form = SubmitQuestion(request.POST)
            if contact_form.is_valid():

                receivers = []
                for user in User.objects.filter(is_superuser=True):
                    receivers.append(user.email)

                send_mail(
                    subject='New Inquiry Received',
                    message='A new inquiry has been submitted. Please respond as soon as possible.',
                    from_email=None,
                    recipient_list=receivers,
                    fail_silently=False
                )
                contact_form.save()
                messages.success(request, f'Your inquiry has been subimtted!')
                return redirect('contact')
        else:
            if newsletter(request):
                return redirect("homepage")

    context = {
        'contact_form': SubmitQuestion(),
        'newsletter_form': NewsletterForm()
        }    

    return render(request, 'fireapp/contact.html', context)