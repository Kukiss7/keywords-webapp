from django import forms
from .models import Website


class NewUrlForm(forms.ModelForm):
    url_input = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows':2, 'placeholder': 'Put some url here...'}
        ),
        max_length=100,
        help_text='This site will be checked for having keywords in their header'  
            ' and if found farther analyse will be provided'
    )

    class Meta:
        model = Website
        fields = ['url']