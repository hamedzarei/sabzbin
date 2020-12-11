from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django_enum_choices.fields import EnumChoiceField
from enum import Enum
from django.core import serializers

# Create your models here.
class UserType(Enum):
    USER = 1 ## کاربر
    SUPPORT = 2 # پشتیبان

class User(AbstractUser):
    uid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    mobile = models.TextField(max_length=15, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=100,blank=True)
    location = models.TextField(max_length=500, blank=True)
    type = EnumChoiceField(UserType)
    uid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def support(self):
        items = Address.objects.all()
        # print(items)
        # i = serializers.serialize('json', Address.objects.all(), fields=('name','type'))
        return items

class PublicUser():
    class Meta:
        model = User
        fields = ['first_name', 'last_name']



