import json

import os

from django.shortcuts import render, get_object_or_404

from catalog.models import Product


# Create your views here.


def home(request):
    products_list = Product.objects.all()
    context = {
        'product_list': products_list,
        'title_name': 'Store',
    }
    return render(request, "catalog/home.html", context)


def contacts(request):
    if request.method == "POST":
        email = request.POST.get("email")
        textarea = request.POST.get("textarea")

        data = {"User": email, "Textarea": textarea}

        json_f = "data.json"

        with open(json_f, "a") as f:
            if os.stat(json_f).st_size == 0:
                json.dump([data], f)
            else:
                with open(json_f) as f_:
                    list_ = json.load(f_)
                    list_.append(data)
                with open(json_f, "w") as f_1:
                    json.dump(list_, f_1)
    context = {
        'title_name': 'Контакты',
    }

    return render(request, "catalog/contacts.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product,
        'title_name': product.product_name,
    }
    return render(request, 'catalog/product_detail.html', context)
