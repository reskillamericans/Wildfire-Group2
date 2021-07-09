from django.contrib import admin
from .models import (
    GuestUser,
    ContentUpdate,
    Categories,
    EmmergencyUpdate,
    HelpRequest,
    Newsletter,
    Faq,
    Contact,
)


@admin.register(GuestUser)
class AdminGuestUser(admin.ModelAdmin):
     list_display = ("first_name", "last_name", "phone_no", "location", "content_update")


@admin.register(ContentUpdate)
class AdminContentUpdate(admin.ModelAdmin):
    list_display = ("title", "content_update", "location", "created_at")
    prepopulated_fields = {"slug":("title",)}


@admin.register(Categories)
class AdminCategories(admin.ModelAdmin):
     list_display = ("help_categories",)


@admin.register(EmmergencyUpdate)
class AdminEmmergencyUpdate(admin.ModelAdmin):
    list_display = ("user", "help_categories", "title", "slug","emmergency", 'created_at')
    prepopulated_fields ={"slug":("title",)}


@admin.register(HelpRequest)
class AdminHelpRequest(admin.ModelAdmin):
    list_display = ("help_categories","first_name","last_name","email","phone_no",
    "emergency_contact_name","relationship","message","location","approved", "created_at")


@admin.register(Newsletter)
class AdminNewsletter(admin.ModelAdmin):
     list_display = ("email",)


@admin.register(Faq)
class AdminFaq(admin.ModelAdmin):
     list_display = ("title", "response")
     #prepopulated_fields = {"slug":("title",)}

@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
     list_display = ("full_name", "phone_no", "message", "email", "created_at")
     
