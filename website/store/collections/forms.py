# make sure this is at the top if it isn't already
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


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


class LogginginForm(AuthenticationForm):
    username = forms.CharField(required=True, label="E-mail")
    # password = forms.CharField(required=True, label="Wachtwoord")

    def __init__(self, *args, **kwargs):
        super(LogginginForm, self).__init__(*args, **kwargs)
        self.fields['password'].label = "Wachtwoord:"

class RegistrationForm(UserCreationForm):
    firstname = forms.CharField(required=True, label="Voornaam:")
    lastname = forms.CharField(required=True, label="Achternaam:")
    email = forms.EmailField(required=True, label="E-mail:")

    class Meta:
        model = User
        fields = ("firstname", "lastname", "email", "password1", "password2")

    def clean_email(self):
        if User.objects.filter(username=self.cleaned_data['email']).exists():
            raise forms.ValidationError('Dit e-mailadres is al ingebruik, vul een ander e-mailadres in')
        return self.cleaned_data['email']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "Wachtwoord:"
        self.fields['password2'].label = "Herhaling wachtwoord:"
        self.fields['password1'].help_text = "Je wachtwoord moet 8 karakters of langer zijn. Gebruik niet alleen cijfers."
        self.fields['password2'].help_text = "Herhaal het wachtwoord"
        self.error_messages = {
            'password_mismatch': ("Oeps! De twee opgegeven wachtwoorden kwamen niet overeen! Probeer het opnieuw!"),
        }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['firstname']
        user.last_name = self.cleaned_data['lastname']
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class CustomerDetails(forms.Form):
    customer_fname = forms.CharField(required=True)
    customer_lname = forms.CharField(required=True)
    customer_email = forms.EmailField(required=True)
    customer_phone = forms.CharField(required=False, max_length=12)

    def __init__(self, *args, **kwargs):
        super(CustomerDetails, self).__init__(*args, **kwargs)
        self.fields['customer_fname'].label = "Voornaam:"
        self.fields['customer_lname'].label = "Achternaam:"
        self.fields['customer_email'].label = "E-mailadres:"
        self.fields['customer_phone'].label = "Telefoonnummer"

class CheckoutForm(forms.Form):
    card_name = forms.CharField(required=True)
    card_number = forms.IntegerField(required=True, max_value=9999999999999999, min_value=1000000000000000)
    card_edm = forms.IntegerField(required=True, max_value=12, min_value=1)
    card_edy = forms.IntegerField(required=True, max_value=9999, min_value=1000)
    card_CVC = forms.IntegerField(required=True, max_value=999, min_value=100)

    def __init__(self, *args, **kwargs):
        super(CheckoutForm, self).__init__(*args, **kwargs)
        self.fields['card_name'].label = "Volledige naam op kaart:"
        self.fields['card_number'].label = "Creditcardnummer:"
        self.fields['card_edm'].label = "Verval datum (mm-jj):"
        self.fields['card_edy'].label = ""
        self.fields['card_CVC'].label = "Controlenummer:"