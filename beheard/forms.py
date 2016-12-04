from django import forms


class LookupForm(forms.Form):

    zip = forms.CharField(label='Zip Code', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))


class BeHeardForm(forms.Form):

    msg = forms.CharField(label='Message Body', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
