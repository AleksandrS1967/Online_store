from django.urls import path

from publication.apps import PublicationConfig
from publication.views import (
    PublicationCreateView,
    PublicationListView,
    PublicationDetailView,
    PublicationUpdateView,
    PublicationDeleteView,
)

app_name = PublicationConfig.name

urlpatterns = [
    path("create/", PublicationCreateView.as_view(), name="create"),
    path("", PublicationListView.as_view(), name="list"),
    path("view/<int:pk>", PublicationDetailView.as_view(), name="view"),
    path("edit/<int:pk>", PublicationUpdateView.as_view(), name="edit"),
    path("delete/<int:pk>", PublicationDeleteView.as_view(), name="delete"),
]
