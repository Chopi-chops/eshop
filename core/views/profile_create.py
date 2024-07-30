from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.views import View

from core.models import *
from core.forms import *


def profile_create(request):
    context = {}
    context["form"] = ProfileForm()

    if request.method == "GET":
        return render(request, 'profile/create.html', context)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Успешно сохранено!")
        return HttpResponse("Ошибка валидации!")


class ProfileCreateView(View):
    def get(self, request):
        context = {}
        context["form"] = ProfileForm()
        return render(request, 'profile/create.html', context)

    def post(self, request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Успешно добавлено!")
            return redirect('/users/')
        messages.warning(request, "Ошибка валидации!")
        return redirect('/users/')

