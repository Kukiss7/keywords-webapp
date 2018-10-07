from django import forms
from .models import Website


class NewUrlForm(forms.ModelForm):
    url = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows':2, 'placeholder': 'Put some url here...'}
        ),
        max_length=100,
        help_text='This site will be checked for having keywords in their header'  
            ' and if found farther analyse will be provided'
        )

     # possible to use builtin django URLField

    # url_input2 = forms.URLField(  
    #     widget=forms.URLInput(
    #         attrs={'rows':2, 'placeholder': 'Put some url here...'}
    #     ),
    #     max_length=100,
    #     help_text='This site will be checked for having keywords in their header'  
    #         ' and if found farther analyse will be provided'
    #     )

    class Meta:
        model = Website
        fields = ['url']