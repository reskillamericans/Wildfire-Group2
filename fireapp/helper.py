from django.contrib.messages.api import success
from django.contrib.messages.constants import SUCCESS
from django.core.checks import messages
from django.conf import settings
from django.shortcuts import redirect, render
from .models import Newsletter
from django.contrib.auth.models import User
from .forms import NewsletterForm
from django.core.mail import send_mail
from django.contrib import messages

def newsletter(request):
    users = User.objects.filter(is_superuser=True)
    if request.method == "POST":
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            subscriber = Newsletter()
            subscriber.email = newsletter_form.cleaned_data["email"]
            if Newsletter.objects.filter(email__icontains=subscriber.email).exists():
                messages.warning(request, f" The email {subscriber.email} already exist in our list.")
                return False
            else:
                subscriber.save()
                send_mail(
                subject="Welcome to Reskill wildfire Subscription.",
                message="You have subscribed to Reskill Americans wildfire subscription.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[str(subscriber.email)],
                fail_silently=False
                )
                messages.success(request, f"Your email {subscriber.email} has been added to our newsletter successfully.")
                for user in users:
                    send_mail(
                        subject="New Reskill Wildfire Subscriber.",
                        message="Dear Admin, You have a new Reskill Americans wildfire subscriber.",
                        from_email=settings.DEFAULT_FROM_EMAIL, 
                        recipient_list= [user.email],
                    )
                    print("Sending mail notification to------->>>", user.email)
                return True
                    
        else:
            messages.warning(request, f"email required")
            return False