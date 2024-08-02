from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.views import View
from core.models import *
from core.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import StaffOnlyMixin


def product_create(request):
    context = {}
    context["product_form"] = ProductForm()

    if request.method == "GET":
        return render(request, 'product_create.html', context)
    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, "Товар добавлен!")
            return redirect('/')
        messages.warning(request, "Ошибка валидации!")
        return redirect('/')


class ProductCreateView(StaffOnlyMixin, View):
    def get(self, request):
        context = {}
        context["product_form"] = ProductForm()
        return render(request, 'product_create.html', context)

    def post(self, request):
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, "Успешно добавлено!")
            return redirect('/')
        messages.warning(request, "Ошибка валидации!")
        return redirect('/')

