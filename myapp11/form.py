from django import forms
class contactform(forms.Form):
    name=forms.CharField(max_length=50)
    email=forms.EmailField()
    message=forms.CharField(max_length=50)