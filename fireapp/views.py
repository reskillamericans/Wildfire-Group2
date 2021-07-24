from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages.api import success
from django.contrib.messages.constants import SUCCESS
from django.core.checks import messages
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.http import JsonResponse

from .forms import NewsletterForm, SubmitQuestion
from .helper import newsletter
from .models import Faq


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

    context = {
        'newsletter_form': NewsletterForm(),
    }
    url_parameter = request.GET.get('q')

    if url_parameter:
       questions = Faq.objects.filter(title__icontains=url_parameter)
    else:
        questions = Faq.objects.all() 

    context['questions'] = questions

    if newsletter(request):
        return redirect("homepage")

    # if it is an ajax request, re-load only the question snippet
    if request.is_ajax():
        html = render_to_string(
            template_name='fireapp/snippets/faq_question_snippet.html',
            context={'questions': questions}
        )

        data_dict = {'html_from_view': html}
        return JsonResponse(data=data_dict, safe=False)
        
    # if it is a regular request, load the whole page
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


def error_404(request, exception):
    return render(request, 'fireapp/404.html')
