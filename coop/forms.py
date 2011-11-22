from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContactForm(forms.Form):
    email_address = forms.EmailField()
    subject = forms.CharField(max_length = 100)
    message = forms.CharField(widget = forms.Textarea(
        attrs = {'class': 'span8'}))
    
    def send(self):
        send_mail(self.cleaned_data['subject'], self.cleaned_data['message'], 
            self.cleaned_data['email_address'], [settings.EMAIL_TO_ADDRESS], 
            fail_silently = False)

