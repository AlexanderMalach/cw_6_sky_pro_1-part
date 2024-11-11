from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from newsletters.models import Mailing, Client
from newsletters.services import send_order_email


class MailingListView(ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    fields = ["status", "message", "frequency", "clients"]
    success_url = reverse_lazy("newsletters:maling_list")

    # fields = ('date_created', 'frequency', 'status', 'message', 'clients',)
    #
    # def get_success_url(self):
    #     return reverse("newsletters:maling_list", args=[self.kwargs.get('pk')])
    #
    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     context_data['client'] = get_object_or_404(Client, pk=self.kwargs.get('pk'))
    #     return context_data
    #
    # def form_valid(self, form):
    #     obj = form.save()
    #     send_order_email(obj)
    #     return super().form_valid(form)


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy("newsletters:maling_list")


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ["status", "message", "frequency", "clients"]
    success_url = reverse_lazy("newsletters:maling_list")

    def get_success_url(self):
        return reverse("newsletters:maling_detail", args=[self.kwargs.get("pk")])
