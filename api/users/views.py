from django.shortcuts import render
from users.models import Address, UserType, User, PublicUser
from response import error_response, ok_response
from rest_framework import viewsets

# Create your views here.
class UsersViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = User.objects.all()

    # specify serializer to be used
    serializer_class = PublicUser

def index(request):
    # a = Address(name='home2', location='12354', user_id=1, type=UserType.USER)
    # a.save()
    user = User()
    return ok_response(user.objects.all())
    address = Address()
    # return
    return ok_response(address.support())
    # i = Address.ob