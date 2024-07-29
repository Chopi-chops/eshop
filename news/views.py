from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import New
from .filters import NewFilter

# Create your views here.
def news_view(request):
    news_list = New.objects.all()
    filter_object = NewFilter(
        data=request.GET,
        queryset=news_list
    )

    context = {"filter_object": filter_object}
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
