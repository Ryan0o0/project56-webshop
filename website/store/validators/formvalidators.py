from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


def postalcode_validator(postalcode):
    if len(postalcode) != 6:  # <--- ZET HIER CONDITIE VOOR POSTCODE
        raise ValidationError(_('Lengte van de postcode moet gelijk zijn aan 6 characters.'))
    else:
        for i in range(0, 4):
            if not (str(postalcode[i]).isdigit()):
                raise ValidationError(_('eerste 4 characters moeten cijfers zijn.'))
        for i in range(4, 5):
            if not (str(postalcode[i]).isalpha()):
                raise ValidationError(_('laatste 2 characters moeten hoofdletters zijn'))

def telephone_validator(telephone):
    if len(telephone) != 8 and len(telephone) != 10:
        raise ValidationError(_('telefoonnummer is niet geldig!'))
    else:
        if not(str(telephone)).isdigit():
            raise ValidationError(_('telefoonnummer is niet geldig'))

