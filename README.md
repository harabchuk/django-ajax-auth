django-ajax-auth
================
This application provides simple Django authentication via AJAX calls. To include it in your application, 
install it with pip ```pip install -e git+https://github.com/FrancoAA/django-ajax-auth.git#egg=django_ajax_auth``` and add ```ajax_auth``` to your INSTALLED_APPS. See the example project fo full usage.

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

##### Logout

```
$.post("ajax_auth/logout/", $(form).serialize(),
    function (data) {
        // Result should be {"success": true}
      })
```

