from django.shortcuts import render, HttpResponse
from .models import New
from django.contrib.auth.models import User

# Create your views here.
def news_view(request):
    news_list = New.objects.all()
    context = {"news": news_list}
    return render(request, 'news.html', context)

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
