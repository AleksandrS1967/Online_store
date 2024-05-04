from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify
from publication.utils.email_yandex import send_message_mail
from publication.models import Publication


# Create your views here.
class PublicationCreateView(CreateView):
    model = Publication
    fields = ('name', 'description', 'image', 'publication_activ', 'counter')
    success_url = reverse_lazy('publication:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name)
            new_mat.save()

        return super().form_valid(form)


class PublicationListView(ListView):
    model = Publication

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication_activ=True)
        return queryset


class PublicationDetailView(DetailView):
    model = Publication

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.counter += 1
        self.object.save()
        if self.object.counter == 100:
            send_message_mail(emails=['sanyastronger@rambler.ru'], text=f"Публикация {self.object.name} набрала 100 просмотров")

        return self.object


class PublicationUpdateView(UpdateView):
    model = Publication
    fields = ('name', 'description', 'image', 'publication_activ', 'counter')
    success_url = reverse_lazy('publication:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('publication:view', args=[self.kwargs.get('pk')])


class PublicationDeleteView(DeleteView):
    model = Publication
    success_url = reverse_lazy('publication:list')
