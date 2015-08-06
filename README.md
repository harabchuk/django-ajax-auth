django-ajax-auth
================
This application provides simple Django authentication via AJAX calls. To include it in your application, 
install it with pip ```pip install -e git+https://github.com/harabchuk/django-ajax-auth.git#egg=django_ajax_auth``` and add ```ajax_auth``` to your INSTALLED_APPS. See the example project fo full usage.

### Sample Usage
##### Login

```
$.post("ajax_auth/login/", $(form).serialize(),
    function (data) {
        // Result should be {"success": true}
      })
      .fail(function (err) {
        // Result will be {"error_msg":<message>,"success":false}
      });
```

##### Register

```
$.post("ajax_auth/register/", $(form).serialize(),
    function (data) {
        // Result should be {"success": true}
      })
      .fail(function (err) {
        // Result will be {"error_msg":<message>,"success":false}
      });
```

To save additional fields into your Profile model or similar you may defile a signal handler in handlers.py
```
from ajax_auth.signals import registration_done
from django.dispatch import receiver


@receiver(registration_done)
def create_profile(sender, **kwargs):
    post = kwargs.get('post')
    user = kwargs.get('user')
    # save additional fields into you Profile model
    # user.profile.phone = post.get('phone')
    # user.save()
```

app.py
```
from django.apps import AppConfig


class YourAppNameConfig(AppConfig):
    name = 'your_app_name'
    verbose_name = 'your_app_name'

    def ready(self):
        import handlers
```

##### Logout

```
$.post("ajax_auth/logout/", $(form).serialize(),
    function (data) {
        // Result should be {"success": true}
      })
```

