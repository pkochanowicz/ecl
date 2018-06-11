from django import forms
from .models import Lecturer


class LecturerCreationForm(forms.Form):
    name = forms.CharField(label='Lecturer name', max_length=32)
    biography = forms.CharField(label='Biography', max_length=500, widget=forms.Textarea, required=False)
    picture = forms.ImageField(label='Picture', required=False)
