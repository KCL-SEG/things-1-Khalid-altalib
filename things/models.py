from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from django.core.validators import MinValueValidator, MaxValueValidator
import django.core.validators as validators

"""In this exercise, you are expected to extend the things app with a basic model that contains a few attributes. 
You can do this exercise as soon as you have completed the videos up to Practice 2.8.

To complete this exercise, extend the application with a model called Thing. 
A Thing entity has the following three attributes:
    name: a short string that identifies a thing.
    description: a slightly longer string that describes a thing.
    quantity: an integer that identifies the number of items of a thing we possess.

Important: You should know that that this exercise requires you to create a class called Thing. 
Model classes must extend django.db.models.Model. Make sure that your model class does.

To complete this exercise, your solution must enforce the following constraints:

    name must be unique, must not be blank, and must consist of 30 characters or less.
    description need not be unique, may be blank, and must consist of 120 characters of less.
    quantity need not be unique, and must be an integer value between 0 and 100 (inclusive). 
    quantity may be 0 and it may be 100, but not less than 0 and not more than 100.
"""


# Create your models here.


def validate_quantity(value):
    if value > 100 or value < 0:
        raise ValidationError(
            _('%(value)s is not a valid quantity'),
            params={'value': value},
        )


class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.CharField(max_length=120, blank=True)
    # quantity must be an integer value between 0 and 100 (inclusive)
    #quantity = models.IntegerField(validators=[validate_quantity])
    quantity = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

