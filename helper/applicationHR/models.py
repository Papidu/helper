from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Positions(models.Model):
    name = models.CharField(max_length=255)

class MyUserManager(BaseUserManager):
    def create_user(self, phone, username, password=None):
        if not phone:
            raise ValueError('User must have a phone number')
        if not username:
            raise ValueError('User must have a username')
        user = self.model(
            phone=phone,
            username=username,
         )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, username, password=None):
        user = self.create_user(
            phone=phone,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser - True
        user.save(using=self._db)
        return user

class Cards(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class User(AbstractBaseUser):
    phone = models.CharField(verbose_name='phone', max_length=20, unique=True)
    username = models.CharField(max_length=30, unique=True)
    name_company = models.CharField(max_length=100)
    position = models.CharField(max_length=255)#
    assigments = models.CharField(max_length=150)#OneToOneField(Cards, on_delete=models.CASCADE)#
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    usertoken = models.CharField(verbose_name='token', max_length=255, unique=True, null=True,blank=True)

    def upload_photo(self, filename):
        path = 'documents/photo/{}'.format(filename)
        return path
    photo = models.ImageField(upload_to=upload_photo, null=True,blank=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username',]

    objects = MyUserManager()

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Summary(models.Model):
    name = models.CharField(max_length=255)
    position = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)
    workedFor = models.CharField(max_length=255)
    recieved = models.DateTimeField(auto_now_add=True)
    scoreBefore = models.FloatField(default=0.0)
    scoreAfter = models.FloatField(default=0.0)
    starred = models.BooleanField(default=False)

class Employees(models.Model):
    name = models.CharField(max_length=255)
    cardId = models.OneToOneField(Cards, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    age = models.IntegerField(default=18)
    salary = models.IntegerField(default=0)
    workedFor = models.CharField(max_length=255)
    recieved = models.DateTimeField(auto_now_add=True)
    score = models.FloatField(default=0.0)
    scoreBefore = models.FloatField(default=0.0)
    scoreAfter = models.FloatField(default=0.0)
    starred = models.BooleanField(default=False)

    def __str__(self):
        return self.name
class Personnel(models.Model):
    name = models.CharField(max_length=250)#models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=250)
    assessment = models.CharField(max_length=250)

    def __str__(self):
        return self.name

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)









#http POST "http://localhost:8000/api/v1/employees/" name='xgfhcg' positionId='xcfvgh' age=23 salary=7 workedFor='dfgh' scoreBefore=4.5 scoreAfter=6.7 starred=False
#http GET "http://localhost:8000/api/v1/employees/"