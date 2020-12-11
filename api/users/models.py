from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django_enum_choices.fields import EnumChoiceField
from enum import Enum
# from rest_framework import serializers
from django.core import serializers
from django.db.models import Count

# Create your models here.
class UserType(Enum):
    USER = 1 ## کاربر
    SUPPORT = 2 # پشتیبان

class User(AbstractUser):
    uid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    mobile = models.TextField(max_length=15, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def address_count(self, query_set):
        return query_set.annotate(Count('address'))

    def public_user_serializer(self, query_set):
        return serializers.serialize('json', query_set, fields={'first_name', 'last_name'})
    def publics_user_serializer(self, query_set):
        return serializers.serialize('json', self.address_count(query_set), fields={'first_name', 'last_name', 'address_count'})

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=100,blank=True)
    location = models.TextField(max_length=500, blank=True)
    type = EnumChoiceField(UserType)
    uid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def support(self):
        items = Address.objects.filter(type=UserType.SUPPORT).values()
        return items

# class PublicUser(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name']



