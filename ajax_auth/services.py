from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError


class AuthHelper(object):

    @staticmethod
    def normalize_username(username_or_email):
        if AuthHelper.is_valid_email(username_or_email):
            return username_or_email(username_or_email)
        return username_or_email

    @staticmethod
    def is_valid_email(email):
        try:
            EmailValidator()(email)
            return True
        except ValidationError:
            return False

    @staticmethod
    def user_name_from_email(email, max_len=30):
        if not email:
            return
        if len(email) < max_len:
            return email
        name = email.split('@')[0]
        if len(name) < max_len:
            return name
        return email[:max_len]