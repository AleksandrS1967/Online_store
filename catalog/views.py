import json

import os

from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView

from catalog.models import Product
from catalog.utils.user_feedback import feedback


# Create your views here.


class ProductListView(ListView):
    model = Product
    extra_context = {'title_name': 'Online Store'}


class ContactsView(View):
    @staticmethod
    def get(request):
        context = {
            'title_name': 'Контакты',
        }

        return render(request, "catalog/contacts.html", context)

    def post(self, request):
        email = request.POST.get("email")
        textarea = request.POST.get("textarea")

        data = {"User": email, "Textarea": textarea}
        json_f = "data.json"
        feedback(json_f, data)

        return self.get(request)


class ProductDetailView(DetailView):
    model = Product
    success_url = reverse_lazy('catalog:home')



# def contacts(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         textarea = request.POST.get("textarea")
#
#         data = {"User": email, "Textarea": textarea}
#
#         json_f = "data.json"
#
#         with open(json_f, "a") as f:
#             if os.stat(json_f).st_size == 0:
#                 json.dump([data], f)
#             else:
#                 with open(json_f) as f_:
#                     list_ = json.load(f_)
#                     list_.append(data)
#                 with open(json_f, "w") as f_1:
#                     json.dump(list_, f_1)
#     context = {
#         'title_name': 'Контакты',
#     }
#
#     return render(request, "catalog/contacts.html", context)
