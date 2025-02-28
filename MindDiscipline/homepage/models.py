from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    phone_number = PhoneNumberField(blank=False, null=False, unique=True, required=True)