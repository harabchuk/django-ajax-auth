import json
import logging

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse
from django.views.generic import View
from django.utils.translation import ugettext as _

from .services import AuthHelper
from .signals import registration_done


log = logging.getLogger(__name__)

try:
    # Django 1.5 and higher supports overriding the default User model
    from django.contrib.auth import get_user_model
except ImportError:
    from django.contrib.auth.models import User

    def get_user_model():
        """
        Return the default User class (for Django < 1.5)
        """
        return User


class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """

    def render_to_json_response(self, context, response_class=HttpResponse):
        """
        Render the context to json
        """
        return self.get_json_response(self.convert_context_to_json(context), response_class)

    def get_json_response(self, content, response_class, **httpresponse_kwargs):
        """
        Create the response object and set the response header
        """
        return response_class(content, content_type='application/json', **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        """
        Convert the content to json
        """
        return json.dumps(context)

    def success_json(self, context=None):
        if not context:
            context = {}
        context['success'] = True
        return self.render_to_json_response(context)

    def error_json(self, context=None, error_msg=None):
        if not context:
            context = {}
        context['success'] = False
        if error_msg:
            context['error_msg'] = error_msg
        return self.render_to_json_response(context)


class LoginView(JSONResponseMixin, View):
    """
    The login view class. This will attempt to authenticate the user
    and will send a response object with the status/error message.
    """

    def post(self, *args, **kwargs):

        context = {}
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        if not username:
            log.warning('[LoginView] username is empty')

        normalized_username = AuthHelper.normalize(username)

        user = authenticate(username=normalized_username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return self.success_json(context)
            else:
                # Return a 'disabled account' error message
                error_msg = _('User account has been disabled')
        else:
            # Return an 'invalid login' error message.
            error_msg = _('Invalid username/password')

        return self.error_json(error_msg=error_msg)


class LogoutView(JSONResponseMixin, View):
    """
    The logout view class. This will log the user out and invalidate the session.
    """

    def post(self, *args, **kwargs):
        logout(self.request)
        return self.success_json()


class RegisterView(JSONResponseMixin, View):
    """
    The register view class. This will attempt to create a user from the
    supplied username and password.

    If the username already exists, a 400 response is sent back
    """

    def post(self, *args, **kwargs):

        context = {}
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        password_confirm = self.request.POST.get('password_confirm')

        if not username:
            log.error('[RegisterView] username is empty')
            return self.error_json(error_msg=_('User name is empty'))

        if password != password_confirm:
            log.debug('[RegisterView] passwords don''t match')
            return self.error_json(error_msg=_('Password does not match the confirm password'))

        email = None
        if AuthHelper.is_email(username):
            email = username
            username = AuthHelper.truncate(username)

        try:
            user = get_user_model().objects.create_user(username, password=password, email=email)
            user = authenticate(username=username, password=password)
            registration_done.send(sender=self.__class__, post=self.request.POST, user=user)
            login(self.request, user)
            log.debug('[RegisterView] registered user {} successfully'.format(username))
            return self.success_json(context)
        except IntegrityError:
            log.warning('[RegisterView] user {} already exists'.format(username))
            return self.error_json(error_msg=_('User already exists'))
        except Exception, e:
            log.exception('[RegisterView] error while creating user "{}". Error message:{}'.format(username, e.message))
            return self.error_json(error_msg=_('Error while registering user'))

