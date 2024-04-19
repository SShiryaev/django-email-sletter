from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView
from mailing.models import Mailing, Client
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'mailing/index.html'
    extra_context = {
        'title': 'Сервис рассылок - Главная'
    }

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     context_data['object_list'] = Breed.objects.all()[:3]
    #     context_data['title'] = 'Сервис рассылок - Главная'
    #     return context_data


class MailingListView(ListView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    fields = ('name', 'send_to', 'send_at', 'periodicity', 'status', 'message',)
    success_url = reverse_lazy('mailing:mailing_list')


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ('name', 'send_to', 'send_at', 'periodicity', 'status', 'message',)
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDetailView(DetailView):
    model = Mailing


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')


class ClientListView(ListView):
    model = Client
