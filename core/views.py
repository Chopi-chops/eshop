from django.shortcuts import render, HttpResponse
from .models import Product
from costumerapp.models import Costumer
from .forms import *
from .filters import ProductFilter


# Create your views here.
def homepage(request):
    product_list = Product.objects.all()
    filter_object = ProductFilter(
        data=request.GET,
        queryset=product_list
    )

    context = {"filter_object": filter_object}

    return render(request, 'index.html', context)


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


def users_list(request):
    user_list = User.objects.all()
    context = {"users": user_list}
    # return HttpResponse('Hello Django!')
    return render(request, 'user_list.html', context)


def product_create(request):
    context = {}
    context["product_form"] = ProductForm()

    if request.method == "GET":
        return render(request, 'product_create.html', context)
    if request.method == "POST":
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            return HttpResponse("Успешно сохранено!")
        return HttpResponse("Ошибка валидации!")


def user_create(request):
    context = {}
    context["user_form"] = UserForm()

    if request.method == "GET":
        return render(request, 'user_create.html', context)
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponse("Успешно сохранено!")
        return HttpResponse("Ошибка валидации!")


def user_cabinet(request, id):
    user = User.objects.get(id=id)
    context = {"user": user}
    return render(request, 'cabinet.html', context)


def search(request):
    keyword = request.GET["keyword"]
    # LIKE
    products = Product.objects.filter(name__icontains=keyword)
    context = {"products": products}
    return render(request, 'search_result.html', context)
