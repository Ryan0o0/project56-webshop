from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


def postalcode_validator(postalcode):
    if len(postalcode) != 6:  # <--- ZET HIER CONDITIE VOOR POSTCODE
        raise ValidationError(_('Lengte van de postcode moet gelijk zijn aan 6 characters.'))
    else:
        for i in range(0, 4):
            if not (str(postalcode[i]).isdigit()):
                raise ValidationError(_('Eerste 4 characters moeten cijfers zijn.'))
        for i in range(4, 5):
            if not (str(postalcode[i]).isalpha()):
                raise ValidationError(_('Laatste 2 characters moeten hoofdletters zijn'))

def telephone_validator(telephone):
    if len(telephone) != 8 and len(telephone) != 10:
        raise ValidationError(_('Telefoonnummer is niet geldig!'))
    else:
        if not(str(telephone)).isdigit():
            raise ValidationError(_('Telefoonnummer is niet geldig'))

def creditcard_validator(cardnumber, length):
    if (len(str(cardnumber))) != length:
        raise ValidationError(_('Kaartnummer is niet geldig!'))
    # else:
    #     for i in range(len(cardnumber)):
    #         if not str(cardnumber[i]).isdigit():
    #             raise ValidationError(_('kaarnummer is niet geldig!'))







