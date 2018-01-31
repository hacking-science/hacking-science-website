from django import forms
from django_markdown.fields import MarkdownFormField
from django_markdown.widgets import MarkdownWidget




class MyCustomForm(forms.Form):
    content = forms.CharField(widget=MarkdownWidget())
    content2 = MarkdownFormField()
