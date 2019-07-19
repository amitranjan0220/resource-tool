from django.forms import ModelForm
from django import forms
from . models import MyResource, Category

CHOICES = [
    ('taf','TAF'),
    ('nanovirt','NANOVIRT'),
    ('ap','AP'),
]

class MyResourceForm(ModelForm):
    class Meta:
        model = MyResource
        fields = ('__all__')
        labels = {
            'rsc_category': ('Category'),
            'rsc_name': ('Name/Serial No.'),
            'rsc_ip': ('IP'),
            'rsc_comment': ('Comment'),
            'rsc_status':('Status')
        }
        

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('__all__')
        