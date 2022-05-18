from django import forms

class InputForm(forms.Form):
    hkuid = forms.CharField(label='HKUID', max_length=20)
    date=forms.DateField(label='Date of diagnosis/onset:')