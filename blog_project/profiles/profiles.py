from django import forms
from .models import profiles

class UpdateProfile(forms.ModelForm):
    class Meta:
        model = profiles
        fields = ['image']