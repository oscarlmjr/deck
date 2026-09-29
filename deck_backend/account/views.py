from django.http import HttpResponse
from django.shortcuts import render

from .models import User


def activateemail(request):
    email = request.GET.get('email', '')
#     email = request.GET.get('', '')
#     email = email_[8:]

    id = request.GET.get('id', '')
#     id = id_[2:]

    print('request.GET = ', request.GET, '\n')
    print('email = ', email, '\n')
    print('id = ', id, '\n')

    if email and id:
        user = User.objects.get(id=id, email=email)
        print('user', user)
        user.is_active = True
        user.save()
    
        return HttpResponse('The user is now activated. You can go ahead and log in!')
    else:
        return HttpResponse('The parameters is not valid!')