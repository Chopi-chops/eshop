from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q

from core.models import *
from core.forms import *


def users_list(request):
    user_list = User.objects.all()
    context = {"users": user_list}
    # return HttpResponse('Hello Django!')
    return render(request, 'user_list.html', context)
