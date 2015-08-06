import django.dispatch

registration_done = django.dispatch.Signal(providing_args=["post", "user"])
