from django.shortcuts import render, HttpResponse
from .models import New

# Create your views here.
def news_view(request):
    news_list = New.objects.all()
    context = {"news": news_list}
    return render(request, 'news.html', context)

