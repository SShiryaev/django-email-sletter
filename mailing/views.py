from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView

from mailing.models import Mailing, Client, Message, MailingLog


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


class ClientCreateView(CreateView):
    model = Client
    fields = ('name', 'email', 'comment',)
    success_url = reverse_lazy('mailing:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('name', 'email', 'comment',)
    success_url = reverse_lazy('mailing:client_list')


class ClientDetailView(DetailView):
    model = Client


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')


class MessageListView(ListView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    fields = ('theme', 'body',)
    success_url = reverse_lazy('mailing:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    fields = ('theme', 'body',)
    success_url = reverse_lazy('mailing:message_list')


class MessageDetailView(DetailView):
    model = Message


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')


class MailingLogListView(ListView):
    model = MailingLog
