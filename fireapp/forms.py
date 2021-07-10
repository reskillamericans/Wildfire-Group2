from django import forms
from django.forms.widgets import EmailInput
from .models import Newsletter, Contact



class NewsletterForm(forms.Form):
    email = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={"placeholder":"Enter email"}))
    email.widget.attrs.update({"id":"web-footer-input-area", "name":"web-footer-input-area"})

    class Meta:
        model: Newsletter
        fields = ["email"]

    def __init__(self, *args, **kwargs):
        super(NewsletterForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = ""

class SubmitQuestion(forms.ModelForm):
    class Meta:
        model= Contact
        fields = ['full_name', 'phone_no', 'message', 'email']
        
        widgets = {
            'full_name': forms.TextInput(attrs={"placeholder":"Full name", "id":"name"}),
            'phone_no': forms.TextInput(attrs={"placeholder":"Phone Number (optional)", "id":"number"}),
            'message': forms.Textarea(attrs={"placeholder":"Contact us for anything related to the website or app.", "id":"message"}),
            'email': forms.EmailInput(attrs={"placeholder":"Email@outlook.com", "id":"email", "class":"subscribe"}),
        }
