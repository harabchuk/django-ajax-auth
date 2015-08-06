from django.apps import AppConfig


class AjaxAuthTestConfig(AppConfig):
    name = 'ajax_auth_test'
    verbose_name = 'ajax_auth_test'

    def ready(self):
        import handlers


