from django.urls import path

from newsletters.apps import NewsletterConfig
from newsletters.views import MailingListView, MailingDetailView, MailingCreateView, MailingDeleteView, \
    MailingUpdateView

app_name = NewsletterConfig.name

urlpatterns = [path("", MailingListView.as_view(), name="maling_list"),
    path("mailing/<int:pk>/", MailingDetailView.as_view(), name="maling_detail"),
    path("mailing/create", MailingCreateView.as_view(), name="maling_create"),
    path("mailing/<int:pk>/update/", MailingUpdateView.as_view(), name="maling_update"),
    path("mailing/<int:pk>/delete/", MailingDeleteView.as_view(), name="maling_delete"), ]
