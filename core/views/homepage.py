from django.shortcuts import render
from core.models import *
from core.forms import *
from core.filters import ProductFilter


class Homepage:  # example
    def get(request):
        product_list = Product.objects.all()

        filter_object = ProductFilter(
            data=request.GET,
            queryset=product_list
        )

        context = {"filter_object": filter_object}
        # messages.add_message(request, messages.INFO, "Hello world")

        # return HttpResponse("Hello Django!")
        return render(request, 'index.html', context)


def homepage(request):
    product_list = Product.objects.all()
    filter_object = ProductFilter(
        data=request.GET,
        queryset=product_list
    )

    context = {"filter_object": filter_object}

    return render(request, 'index.html', context)
