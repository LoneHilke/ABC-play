from django import forms
from dansk.models import  Alfabet


class GætForm(forms.Form):
    gæt = forms.CharField(label="Hvad forestiller billedet?", max_length=50)