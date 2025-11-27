from django import forms
from .models import Letter, Words

class EkstraForm(forms.ModelForm):
  ord = forms.CharField(
    widget=forms.TextInput(
      attrs={'placeholder': 'Tilføj...'}))

  class Meta:
    model = Words 
    fields = '__all__'