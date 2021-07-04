from django.contrib.messages.api import success
from django.contrib.messages.constants import SUCCESS
from django.core.checks import messages
from django.shortcuts import HttpResponse, redirect, render
from .models import Newsletter
from .forms import NewsletterForm
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings



# Create your views here.
def index(request):
    return HttpResponse("<h1>Wildfire App 2</h1>")


# Newsletter view
def news_letter_view(request):
    newsletter_form = ""
    template_name = "newsletter/index.html"
    if request.method == "POST":
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            subscriber = Newsletter()
            subscriber.email = newsletter_form.cleaned_data["email"]
            if Newsletter.objects.filter(email__icontains=subscriber.email).exists():
                messages.warning(request, f" The email {subscriber.email} already exist in our list")
                return redirect("news-letter")
            else:
                subscriber.save()
                send_mail(
                subject="Welcome to Reskill wildfire Subscription",
                message="You have subscribed to Reskill Americans wildfire subscription",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[str(subscriber.email)],
                fail_silently=False
                ),
                messages.success(request, f"your email {subscriber.email} has been added to our newsletter successfully")
                return redirect("news-letter")
        else:
            messages.warning(request, f"email required")
            return redirect("news-letter")
    else:
        newsletter_form = NewsletterForm()
    context = {"newsletter_form":newsletter_form}
    return render(request, template_name, context)

            