from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import user_avatar_path

class UserProfilePlus(models.Model):

    USER_CAT = (
        ('T', 'Coach'),
        ('S', 'Sportsman'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, to_field='id')
    user_cat = models.CharField(max_length=1, choices=USER_CAT, default='V')
    avatar = models.ImageField(blank=True, upload_to=user_avatar_path, default='authentication/static/svg/person-circle.svg')
    first_name = models.CharField(blank=True, max_length=150, null=True)
    last_name = models.CharField(blank=True, max_length=150, null=True)
    phone_number = models.CharField(blank=True, max_length=20, null=True)
   
    class Meta:
        verbose_name = 'User Profile Plus'
        verbose_name_plural = 'User Profiles Plus'

    def __str__(self) -> str:
        return self.user.username
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfilePlus.objects.create(user=instance)