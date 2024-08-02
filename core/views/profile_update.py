from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from core.models import *
from core.forms import *


def profile_update(request, id):
    context = {}
    profile_object = Profile.objects.get(id=id)
    if request.user != profile_object.user:
        messages.error(request, "Нет доступа")
        return redirect('/')
    context["form"] = ProfileForm(instance=profile_object)

    if request.method == "GET":
        return render(request, "profile/update.html", context)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile_object)
        if form.is_valid():
            form.save()
            messages.success(request, "Успешно обновлено!")
            return redirect('/users/')
        messages.warning(request, "Ошибка валидации!")
        return redirect('/users/')
