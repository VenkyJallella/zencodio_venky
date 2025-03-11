from django import forms
from .models import Contact_Me, Payment,NewsletterSubscriber

class contact_form(forms.ModelForm):
    class Meta:
        model = Contact_Me
        fields = ['name','email','message']

class payments_form(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['name','email','phone','address']

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']