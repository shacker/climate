from django import forms


class LookupForm(forms.Form):

    zip = forms.CharField(
        label='', required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your zip code'}))

    def clean_zip(self):
        data = self.cleaned_data['zip']
        if not data.isdigit():
            raise forms.ValidationError("Zip code must be all digits")
        if not len(data) == 5:
            raise forms.ValidationError("Zip code must be five digits")
        return data


class BeHeardForm(forms.Form):

    msg = forms.CharField(
        label='',
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': "Share something about who you are and why you're Pro-Climate"}
            ),
        )
    your_name = forms.CharField(
        label='Sincerely,',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Your Name'},
        )
    )
    your_town = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'City, State'},
        )
    )
    your_email = forms.EmailField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'you@example.com'},
        )
    )
