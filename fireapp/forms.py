from django import forms
from .models import Newsletter



class NewsletterForm(forms.Form):
    email = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={"placeholder":"Enter email"}))
    email.widget.attrs.update({"id":"web-footer-input-area", "name":"web-footer-input-area"})

    class Meta:
        model: Newsletter
        fields = ["email"]

    