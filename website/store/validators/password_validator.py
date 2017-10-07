from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _, ungettext

class MinimumLengthValidator(object):
    """
    We overschrijven hier de default MinimumLengthValidator, aangezien deze alleen engelse error messages kan geven.
    """
    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                ungettext(
                    "Dit wachtwoord is te kort, het moet tenminste %(min_length)d karakters bevatten",
                    "Dit wachtwoord is te kort, het moet tenminste %(min_length)d karakters bevatten.",
                    self.min_length
                ),
                code='password_too_short',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return ungettext(
            "Dit wachtwoord is te kort, het moet tenminste %(min_length)d karakters bevatten.",
            "Dit wachtwoord is te kort, het moet tenminste %(min_length)d karakters bevatten.",
            self.min_length
        ) % {'min_length': self.min_length}

class NumericPasswordValidator(object):
    """
    Hier overschrijven we weer de default validator om de messages in het Nederlands te krijgen
    """
    def validate(self, password, user=None):
        if password.isdigit():
            raise ValidationError(
                _("Dit wachtwoord bestaat enkel uit nummers, zorg dat uw wachtwoord ook letters bevat."),
                code='password_entirely_numeric',
            )

    def get_help_text(self):
        return _("Dit wachtwoord bestaat enkel uit nummers, zorg dat uw wachtwoord ook letters bevat.")
