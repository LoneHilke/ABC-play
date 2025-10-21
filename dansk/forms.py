from django import forms
from .models import Bogstav, Alfabet

class GætForm(forms.Form):
    gæt = forms.CharField(label="Hvad forestiller billedet?", max_length=50)

class EkstraForm(forms.ModelForm):
  ord = forms.CharField(
    widget=forms.TextInput(
      attrs={'placeholder': 'Tilføj...'}))

  class Meta:
    model = Alfabet 
    fields = '__all__'