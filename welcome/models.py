from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
<<<<<<< HEAD
#from awesome_avatar.fields import AvatarField
=======
from awesome_avatar.fields import AvatarField
>>>>>>> b609d75f2eeb607948a1ca4f768e20c6a4034f73

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
<<<<<<< HEAD
    avatar = models.ImageField(upload_to='avatars')
=======
    avatar = AvatarField(upload_to='avatars', width=100, height=100)
>>>>>>> b609d75f2eeb607948a1ca4f768e20c6a4034f73
    description = models.CharField(max_length=100, blank=True)
    vk = models.CharField(max_length=50, blank=True)
    telegram = models.CharField(max_length=50, blank=True)
    whatsapp = models.CharField(max_length=50, blank=True)
    viber = models.CharField(max_length=50, blank=True)
    insta = models.CharField(max_length=50, blank=True)
    skype = models.CharField(max_length=50, blank=True)

class Images(models.Model):
    image = models.ImageField(upload_to='images')

    #def __str__(self):
        #return self.user

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
 #   instance.profile.save()