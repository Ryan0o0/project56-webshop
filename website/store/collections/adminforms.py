from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Max

from store.models import Customers, Address


class AdminRegistrationForm(UserCreationForm):
    firstname = forms.CharField(required=True, label="Voornaam:")
    lastname = forms.CharField(required=True, label="Achternaam:")
    email = forms.EmailField(required=True, label="E-mail:")
    isstaff = forms.BooleanField(required=False, label='Is medewerker:')

    class Meta:
        model = User
        fields = ("firstname", "lastname", "email", "password1", "password2")

    def clean_email(self):
        usernameEmail = self.cleaned_data['email']
        if User.objects.filter(username=usernameEmail).exists():
            raise forms.ValidationError('Dit e-mailadres is al ingebruik, vul een ander e-mailadres in')
        return self.cleaned_data['email']

    def __init__(self, *args, **kwargs):
        super(AdminRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "Wachtwoord:"
        self.fields['password2'].label = "Herhaling wachtwoord:"

    def save(self, commit=True):
        user = super(AdminRegistrationForm, self).save(commit=False)
        maxID = Customers.objects.all().aggregate(Max('customerID'))
        if maxID.get('customerID__max') == None:
            user.id = 1
        else:
            user.id = maxID.get('customerID__max') + 1

        user.first_name = self.cleaned_data['firstname']
        user.last_name = self.cleaned_data['lastname']
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        user.is_staff = self.cleaned_data['isstaff']

        #Every new User in the Auth table also requires a Customer entity
        newEntryCustomer = Customers(customerID=user.id, email=user.email, name=user.first_name, surname=user.last_name,
                                  telephone='nvt', isRegistered=True)
        newEntryCustomer.save()

        #Every Customer requires an Address entity
        newEntryAddress = Address(customerID=Customers(customerID=user.id))
        newEntryAddress.save()

        if commit:
            user.save()

        return user