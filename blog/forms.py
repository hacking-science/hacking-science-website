from django import forms
from models import Subscribe
from django.forms import ModelForm


class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = ['first_name', 'last_name', 'email_address']

    def is_valid(self):
        """"Returns True if the form has no erros, else false"""
        return self.is_bound and not self.errors
