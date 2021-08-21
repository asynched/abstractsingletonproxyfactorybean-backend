import re
from django.contrib.auth.password_validation import CommonPasswordValidator
from django.core.exceptions import ValidationError


class UserValidator:
    def validate_username(username):
        if not re.match(r'^[a-zA-Z0-9]{5,16}$', username):
            raise ValidationError('Username is invalid.')

    def validate_name(name):
        if not re.match(r'^[^\s]{3,16}$', name):
            raise ValidationError('Name is invalid.')

    def validate_password(password):
        if len(password) < 8:
            raise ValidationError('Password must be at least 8 characters')

        CommonPasswordValidator().validate(password)
