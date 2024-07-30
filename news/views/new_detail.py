from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import DetailView
from django.views import View
from news.models import New



class NewDetailView(View):
    def get(self, request, pk):
        new_object = New.objects.get(pk=pk)
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