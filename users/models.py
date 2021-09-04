from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female')
    ]
    gender = models.PositiveSmallIntegerField(verbose_name="Gender", choices=GENDER_CHOICES, default=GENDER_FEMALE)
    user = models.OneToOneField(User, verbose_name=('user'), on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(('age'))
    avatar = models.ImageField(('avatar'), blank=True, upload_to='avatars')
    phone_number = models.PositiveBigIntegerField(('phone number'), unique=True)
    bio = models.TextField(('bio'), blank=True)

    class Meta:
        db_table = 'profiles'
        verbose_name = ('Profile')
        verbose_name_plural = ('Profiles')

    def __str__(self):
        return '{}'.format(self.user)

