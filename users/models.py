from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female')
    ]
    gender = models.PositiveSmallIntegerField(verbose_name="Gender", choices=GENDER_CHOICES, default=GENDER_FEMALE)
    user = models.OneToOneField(User, verbose_name="User", on_delete=models.CASCADE)
    age = models.IntegerField(verbose_name="Age", default=0)
    avatar = models.ImageField(verbose_name="Avatar", blank=True, upload_to='avatars')
    phone_number = models.PositiveBigIntegerField(verbose_name="Phone Number", default=00000000000)
    bio = models.TextField(verbose_name="Bio", blank=True)

    class Meta:
        db_table = 'profiles'
        verbose_name = ('Profile')
        verbose_name_plural = ('Profiles')

    def __str__(self):
        return '{}'.format(self.user)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()



