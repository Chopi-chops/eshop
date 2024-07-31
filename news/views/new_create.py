from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import DetailView
from django.views import View
from news.models import New
from news.forms import *


def new_create(request):
    if request.method == "GET":
        return render(request, 'new_create.html')
    elif request.method == "POST":
        # 1. Считывание данные с формы
        data = request.POST
        title = data["new_title"]
        text = data["new_article"]

        # 2. Сохранение этих данных в БД
        new_object = New.objects.create(
            title=title,
            article=text,
        )
        messages.success(request, "Новость добавлена!")
        return redirect(f'/new/{new_object.id}/')


class NewCreateView(View):
    def get(self, request):
        context = {}
        context["form"] = NewForm()
        return render(request, 'new_create.html', context)

    def post(self, request):
        form = NewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Успешно добавлено!")
            return redirect('/news/')
        messages.warning(request, "Ошибка валидации!")
        return redirect('/news/')
