import json

import os

from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version, Category
from catalog.utils.user_feedback import feedback


# Create your views here.


class ProductListView(ListView):
    model = Product
    extra_context = {"title_name": "Online Store"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        products = Product.objects.all()
        category = Category.objects.all()

        for product in products:
            versions = Version.objects.filter(product=product)
            activity = versions.filter(current_version=True)
            if activity:
                product.activ_version = activity.last().version_name
            else:
                product.activ_version = "..."
        context["product_list"] = products
        context["category_list"] = category

        return context


class ContactsView(View):
    @staticmethod
    def get(request):
        context = {
            "title_name": "Контакты",
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
    success_url = reverse_lazy("catalog:home")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:home")


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        versions = Version.objects.filter(product=self.object)
        context["count_version"] = len(versions)

        return context

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(
            Product, Version, form=VersionForm, extra=0
        )
        if self.request.method == "POST":
            context["formset"] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context["formset"] = VersionFormset(instance=self.object)
        versions = Version.objects.filter(product=self.object)
        context["count_version"] = len(versions)
        return context

    def form_valid(self, form):
        formset = self.get_context_data()["formset"]

        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy("catalog:home")
