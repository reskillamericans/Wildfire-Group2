from django.contrib.messages.api import success
from django.contrib.messages.constants import SUCCESS
from django.core.checks import messages
from django.conf import settings
from django.shortcuts import redirect, render
from .models import Newsletter, Faq
from django.contrib.auth.models import User
from .forms import NewsletterForm, SubmitQuestion
from django.core.mail import send_mail
from django.contrib import messages



# Newsletter view
def index(request):
    users = User.objects.filter(is_superuser=True)
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
                return redirect("homepage")
                    
        else:
            messages.warning(request, f"email required")
            return redirect("homepage")
    else:
        newsletter_form = NewsletterForm()
    context = {"newsletter_form":newsletter_form}
    return render(request, template_name, context)


# About Us
def about_us(request):
    template_name = "fireapp/about-us.html"
    return render(request, template_name)


# freequently asked question(faq)
def faq(request):

    context = {
        'questions' : Faq.objects.all() 
    }

    return render(request, 'fireapp/faq.html', context)
def contact(request):
    if request.method =='POST':
        form = SubmitQuestion(request.POST)
        if form.is_valid():

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
            form.save()
            messages.success(request, f'Your inquiry has been subimtted!')
            return redirect('contact')
    else:
        form = SubmitQuestion()

    return render(request, 'fireapp/contact.html', {'form':form})