from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from mailing.models import Mailing, Client, Message, MailingLog
from mailing.forms import MailingForm


class IndexView(TemplateView, LoginRequiredMixin):
    template_name = 'mailing/index.html'
    extra_context = {
        'title': 'Сервис рассылок - Главная'
    }

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     context_data['object_list'] = Breed.objects.all()[:3]
    #     context_data['title'] = 'Сервис рассылок - Главная'
    #     return context_data


class MailingListView(LoginRequiredMixin, ListView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Mailing

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        user = self.request.user
        if not user.is_superuser and not user.groups.filter(name='manager').exists():
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class MailingCreateView(LoginRequiredMixin, CreateView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Mailing

    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        mailing = form.save()
        user = self.request.user
        mailing.owner = user
        mailing.save()
        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UpdateView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Mailing
    fields = ('name', 'send_to', 'send_at', 'periodicity', 'status', 'message',)
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDetailView(LoginRequiredMixin, DetailView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Mailing


class MailingDeleteView(LoginRequiredMixin, DeleteView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')


class ClientListView(LoginRequiredMixin, ListView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Client
    fields = ('name', 'email', 'comment',)
    success_url = reverse_lazy('mailing:client_list')


class ClientUpdateView(LoginRequiredMixin, UpdateView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Client
    fields = ('name', 'email', 'comment',)
    success_url = reverse_lazy('mailing:client_list')


class ClientDetailView(LoginRequiredMixin, DetailView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Client


class ClientDeleteView(LoginRequiredMixin, DeleteView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Client
    success_url = reverse_lazy('mailing:client_list')


class MessageListView(LoginRequiredMixin, ListView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Message
    fields = ('theme', 'body',)
    success_url = reverse_lazy('mailing:message_list')


class MessageUpdateView(LoginRequiredMixin, UpdateView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Message
    fields = ('theme', 'body',)
    success_url = reverse_lazy('mailing:message_list')


class MessageDetailView(LoginRequiredMixin, DetailView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Message


class MessageDeleteView(LoginRequiredMixin, DeleteView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Message
    success_url = reverse_lazy('mailing:message_list')


class MailingLogListView(LoginRequiredMixin, ListView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = MailingLog
