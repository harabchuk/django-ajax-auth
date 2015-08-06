from ajax_auth.signals import registration_done
from django.dispatch import receiver


@receiver(registration_done)
def create_profile(sender, **kwargs):
    post = kwargs.get('post')
    print "Creating profile"
