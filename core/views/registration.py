from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from core.models import *
from core.forms import *


def registration(request):
    context = {}

    if request.method == "POST":
        # create user object
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            user_object = reg_form.save()
            password = request.POST["password"]
            user_object.set_password(password)
            user_object.save()
            return redirect('/')
        return HttpResponse("Ошибка валидации")

    reg_form = RegistrationForm()
    context["reg_form"] = reg_form
    return render(request, 'profile/registration.html', context)
