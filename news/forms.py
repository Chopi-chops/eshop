from django import forms
from .models import New


class NewForm(forms.ModelForm):
    class Meta:
        model = New
        fields = [
            'title',
            'article',
        ]
