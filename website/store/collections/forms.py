# make sure this is at the top if it isn't already
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Voor- en achternaam:"
        self.fields['contact_email'].label = "E-mailadres:"
        self.fields['content'].label = "Toelichting"


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = {
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
