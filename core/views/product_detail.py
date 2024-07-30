from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q
from django.views import View

from core.models import *
from costumerapp.models import Costumer
from core.forms import *


class ProductDetailView(View):
    def get(self, request, pk):
        product_object = Product.objects.get(pk=pk)
        product_object.views_qty += 1
        if request.user.is_authenticated:
            user = request.user
            if not Costumer.objects.filter(user=user).exists():
                costumer = Costumer.objects.create(
                    name=user.username,
                    age=0,
                    gender='-',
                    user=user,
                )
            costumer = user.costumer
            product_object.costumer_views.add(costumer)
        product_object.save()
        context = {
            "product": product_object,
        }
        return render(request, 'product_detail.html', context)


def product_detail(request, id):
    # SELECT * FROM Product WHERE id = $id; -- где id - число с url
    product_object = Product.objects.get(id=id)

    # Увеличение просмотра
    product_object.views_qty += 1

    # Уникальные просмотры
    if request.user.is_authenticated:
        user = request.user
        if not Costumer.objects.filter(user=user).exists():
            costumer = Costumer.objects.create(
                name=user.username,
                age=0,
                gender='-',
                user=user,
            )
        costumer = user.costumer
        product_object.costumer_views.add(costumer)
        # product_object.costumer_views.add(request.user.costumer)

    # Сохранение в БД
    product_object.save()

    context = {
        "product": product_object,
    }
    return render(request, 'product_detail.html', context)

