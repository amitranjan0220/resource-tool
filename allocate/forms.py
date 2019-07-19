from django import forms
from django.forms import ModelForm
from . models import AllocateResource, SearchByResource, SearchByUser
from my_resource.models import MyResource, Category
from django.contrib.auth.models import User


class UserSearchForm(ModelForm):
    class Meta:
        model = SearchByUser
        fields = ('__all__')

class ResourceSearchForm(ModelForm):
    class Meta:
        model = SearchByResource
        fields = ('category','resource')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['resource'].queryset = MyResource.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                cat = Category.objects.get(pk=category_id)
                self.fields['resource'].queryset = MyResource.objects.filter(rsc_category=cat)
            except (ValueError, TypeError):
                pass
        else:
            pass