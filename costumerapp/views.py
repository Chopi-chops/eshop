from django.shortcuts import render, HttpResponse
from .models import Costumer

# Create your views here.
def costumer_view(request):
    costumer_list = Costumer.objects.all()
    context = {"costumers": costumer_list}
    return render(request, 'costumers.html', context)
