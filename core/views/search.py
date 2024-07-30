from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q

from core.models import *
from core.forms import *


def search(request):
    keyword = request.GET["keyword"]
    # WHERE name LIKE '%keyword%' OR description LIKE '%keyword%'
    products = Product.objects.filter(
        Q(name__icontains=keyword) |
        Q(description__icontains=keyword) |
        Q(category__name__icontains=keyword)
    )
    context = {"products": products}
    return render(request, 'search_result.html', context)
