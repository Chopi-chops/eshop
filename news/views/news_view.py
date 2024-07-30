from django.shortcuts import render
from news.models import New
from news.filters import NewFilter


def news_view(request):
    news_list = New.objects.all()
    filter_object = NewFilter(
        data=request.GET,
        queryset=news_list
    )

    context = {"filter_object": filter_object}
    return render(request, 'news.html', context)