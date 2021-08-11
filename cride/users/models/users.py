"""USer model"""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# utilities
from cride.utils.models import CRideModel

class User(CRideModel, AbstractUser):
    """ USer model.
    Extend from DJango's Abstrac User, change the username field to
    email and add some extar fields
    """
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages = {
            'unique': 'A user with than email already exists.'
        }
    )

    # Validación a un campo
    phone_regex = RegexValidator(
       regex=r'\+?1?\d{9,15}$',
       message='Phone number must be entered in tle format: +91234567890. Up to 15 digits allowed.' 
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client status',
        default=True,
        help_text=(
            'Help easily distinguish users and perfom queries. '
            'Cclients are the main type of user'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text='Set to true when the user have verified its email addres.'
    )

    def __str__(self):
        """ Return username."""
        return self.username

    def get_short_name(self):
        """ Return username"""
        return self.username