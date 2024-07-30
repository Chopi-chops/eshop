from django.shortcuts import render
from django.views.generic import DetailView

from core.models import *
from core.forms import *


class UserCabinet(DetailView):
    model = User
    template_name = 'cabinet.html' # auth/user_detail.html


# def user_cabinet(request, id):
#     user = User.objects.get(id=id)
#     context = {"user": user}
#     return render(request, 'cabinet.html', context)
