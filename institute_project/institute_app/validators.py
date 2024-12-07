from django.core.exceptions import ValidationError

def validate_postal_code(value):
    if not (value.isdigit() and len(value) == 6):
        raise ValidationError('Postal code must be a 6-digit number.')