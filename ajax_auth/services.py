from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError


class AuthHelper(object):

    @staticmethod
    def normalize(username_or_email):
        if AuthHelper.is_email(username_or_email):
            return AuthHelper.truncate(username_or_email)
        return username_or_email

    @staticmethod
    def is_email(email):
        try:
            EmailValidator()(email)
            return True
        except ValidationError:
            return False

    @staticmethod
    def truncate(email, max_len=30):
        """
        If email exceeds max_len truncates it
        :return: email if it is shorter than max_len or first part of email or truncated first part 
        """
        if not email:
            return
        if len(email) < max_len:
            return email
        name = email.split('@')[0]
        if len(name) < max_len:
            return name
        return email[:max_len]