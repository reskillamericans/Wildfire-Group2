from django.contrib.messages.api import success
from django.contrib.messages.constants import SUCCESS
from django.core.checks import messages
from django.conf import settings
from django.shortcuts import redirect, render
from .models import Newsletter, Faq
from .forms import NewsletterForm
from django.core.mail import send_mail
from django.contrib import messages



# Newsletter view
def index(request):
    newsletter_form = ""
    template_name = "fireapp/index.html"
    if request.method == "POST":
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            subscriber = Newsletter()
            subscriber.email = newsletter_form.cleaned_data["email"]
            if Newsletter.objects.filter(email__icontains=subscriber.email).exists():
                messages.warning(request, f" The email {subscriber.email} already exist in our list.")
                return redirect("homepage")
            else:
                subscriber.save()
                send_mail(
                subject="Welcome to Reskill wildfire Subscription.",
                message="You have subscribed to Reskill Americans wildfire subscription.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[str(subscriber.email)],
                fail_silently=False
                ),
                messages.success(request, f"Your email {subscriber.email} has been added to our newsletter successfully.")
                return redirect("homepage")
        else:
            messages.warning(request, f"email required")
            return redirect("homepage")
    else:
        newsletter_form = NewsletterForm()
    context = {"newsletter_form":newsletter_form}
    return render(request, template_name, context)


# freequently asked question(faq)
def faq(request):

    context = {
        'questions' : Faq.objects.all() 
    }

    return render(request, 'fireapp/faq.html', context)