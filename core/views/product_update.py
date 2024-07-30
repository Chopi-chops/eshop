from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from core.models import *
from core.forms import *


def product_update(request, id):
    context = {}
    product_object = Product.objects.get(id=id)
    context["form"] = ProductForm(instance=product_object)

    if request.method == "GET":
        return render(request, "product/update.html", context)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product_object)
        if form.is_valid():
            form.save()
            messages.success(request, "Успешно обновлено!")
            return redirect('/')
        messages.warning(request, "Ошибка валидации!")
        return redirect('/')
