from django import forms

from .models import Entity, Property


class EntityForm(forms.ModelForm):
    
    class Meta:
        model = Entity
        fields = ('modified_by', 'value')
