from django import forms

REQUEST_CHOICES = (
    ('Anime', 'Anime'),
    ('Movie', 'Movie'),
    ('Others', 'Others'),
)


class RequestForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'col-md-6 form-it',
        'placeholder': 'Naruto Uzumaki'
    }))
    email_address = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'col-md-6 form-it',
        'placeholder': 'yourname@example.com'
    }))
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'col-md-6 form-it',
        'placeholder': 'Your Name'
    }))
    season = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'col-md-6 form-it',
        'placeholder': 'Season 1'
    }), required=False)
    choice = forms.ChoiceField(widget=forms.Select(), choices=REQUEST_CHOICES)
    message = forms.CharField(widget=forms.TextInput(attrs={
        "rows": 4,
        'placeholder': 'Have any message for us?'
    }), required=False)
