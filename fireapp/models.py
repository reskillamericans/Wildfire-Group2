from django.db import models
from django.db.models import fields
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone




#users who wish to get regular update mails can supply their emails for news letters.
class Newsletter(models.Model):
    email = models.EmailField(max_length=150, unique=True)
    
    def __str__(self):
        return f"{self.email}"

    def get_absolute_url(request):
        return reverse('news-letter')


# both registered and guest users can add contents or updates with this form.
class ContentUpdate(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    content_update = models.TextField(blank=True)
    location = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.title}"


# forms to be filled by guest users to post fire updates
class GuestUser(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_no = models.IntegerField()
    location = models.CharField(max_length=200)
    content_update = models.ForeignKey(ContentUpdate, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name, self.last_name}"


############################################################################################
class Categories(models.Model):
    help_categories = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.help_categories}"


# only admins can create this update and serve to the update page at the front end to all users.
class EmmergencyUpdate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    help_categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    emmergency = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"


# registered users request for help based on the project flowchat requirements
class HelpRequest(models.Model):
    help_categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    phone_no = models.IntegerField()
    emergency_contact_name = models.CharField(max_length=200)
    relationship = models.CharField(max_length=200)
    message = models.TextField()
    location = models.CharField(max_length=200)
    approved = models.BooleanField(False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name, self.last_name}"


# Frequently Asked Questions. to be extended to the frontend.Each details can be expanded to be read in full.
class Faq(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=300)
    message = models.TextField()
    response = models.TextField()

    def __str__(self):
        return f"{self.title}"
