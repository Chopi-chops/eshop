from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib import messages
from news.models import New



class NewDetailView(View):
    def get(self, request, pk):
        try:
            new_object = New.objects.get(pk=pk)
        except New.DoesNotExist:
            messages.error(request, "Новость не найдена")
            return redirect('/')
        new_object.views += 1
        if request.user.is_authenticated:
            new_object.user_views.add(request.user)
        new_object.save()
        context = {
            "new": new_object,
        }
        return render(request, 'news_detail.html', context)


def new_detail(request, id):
    new_object = New.objects.get(id=id)

    # Увеличение просмотра
    new_object.views += 1

    # Уникальные просмотры
    if request.user.is_authenticated:
        new_object.user_views.add(request.user)

    # Сохранение в БД
    new_object.save()

    context = {
        "new": new_object,
    }
    return render(request, 'news_detail.html', context)