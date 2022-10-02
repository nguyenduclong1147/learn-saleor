from django.db import models
from .validators import validate_possible_number
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class PossiblePhoneNumberField(PhoneNumberField):
    """Less strict field for phone numbers written to database."""

    default_validators = [validate_possible_number]

class Address(models.Model):
    phone = PossiblePhoneNumberField(blank=True, default="", db_index=True)