from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


def postalcode_validator(postalcode):
    postalcode = postalcode_reformer(postalcode)
    if len(postalcode) != 6:  # <--- ZET HIER CONDITIE VOOR POSTCODE
        raise ValidationError(_('Lengte van de postcode moet gelijk zijn aan 6 characters.'))
    else:
        for i in range(0, 4):
            if not (str(postalcode[i]).isdigit()):
                raise ValidationError(_('Eerste 4 characters moeten cijfers zijn.'))
        for i in range(4, 5):
            if not (str(postalcode[i]).isalpha()):
                raise ValidationError(_('Laatste 2 characters moeten hoofdletters zijn'))

def postalcode_reformer(postalcode):
    if postalcode[4].isspace():
        postalcode = postalcode[:3] + postalcode[5:]
    postalcode = postalcode[:3] + postalcode[4:].upper()
    return postalcode

def telephone_validator(telephone):
    list = [8, 10]
    if telephone == "nvt" or len(telephone) == 0:
        return telephone
    elif len(str(telephone)) not in list:
        raise ValidationError(_('Telefoonnummer is niet geldig!'))
    else:
        if not(str(telephone)).isdigit():
            raise ValidationError(_('Telefoonnummer is niet geldig!'))

def creditcard_validator(cardnumber, length):
    if (len(str(cardnumber))) != length:
        raise ValidationError(_('Kaartnummer is niet geldig!'))
    else:
        if cardnumber <= 0:
            raise ValidationError(_('Kaartnummer is niet geldig!'))
    #     for i in range(len(cardnumber)):
    #         if not str(cardnumber[i]).isdigit():
    #             raise ValidationError(_('kaarnummer is niet geldig!'))







