from django.shortcuts import render
from users.models import Address, UserType, User
from response import error_response, ok_response
from rest_framework import viewsets
from django.db.models import Count

def index(request):
    # a = Address(name='home2', location='12354', user_id=1, type=UserType.USER)
    # a.save()
    user = User()
    # a = Address()
    # a.support()
    # print(User.objects.values())
    user = User()
    return ok_response(user.publics_user_serializer(User.objects.all()))
    # return ok_response(PublicUser(User.objects))
    return ok_response(User.objects.annotate(Count('address')).values())
    address = Address()
    # return
    return ok_response(address.support())
    # i = Address.ob