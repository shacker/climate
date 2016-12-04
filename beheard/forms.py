from django import forms


class LookupForm(forms.Form):

    zip = forms.CharField(label='Zip Code', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_zip(self):
        data = self.cleaned_data['zip']
        if not data.isdigit():
            raise forms.ValidationError("Zip code must be all digits")
        if not len(data) == 5:
            raise forms.ValidationError("Zip code must be five digits")
        return data


class BeHeardForm(forms.Form):

    msg = forms.CharField(
        label='Message Body',
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        initial="foo")
