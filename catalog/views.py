import json

import os

from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
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


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

