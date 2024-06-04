import random
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from mailing.models import Mailing, Client, Message, MailingLog
from blog.models import Material
from mailing.forms import MailingForm, MailingManagerForm, ClientForm, MessageForm


class IndexView(TemplateView, LoginRequiredMixin):
    template_name = 'mailing/index.html'
    extra_context = {
        'title': 'Сервис рассылок - Главная'
    }

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        mailing = Mailing.objects.all()
        clients = Client.objects.all()
        context['count_mailing'] = mailing.count()
        context['is_active_mailing'] = mailing.filter(status=Mailing.Status.LAUNCHED).count()
        context['unique_clients'] = clients.values('email').distinct().count()
        context['blogs'] = Material.objects.all()
        context['blog_list'] = list(context['blogs'])
        random.shuffle(context['blog_list'])
        context['shuffled_blog_list'] = context['blog_list'][:3]
        return context


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

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        user = self.request.user
        form.fields['send_to'].queryset = Client.objects.filter(owner=user)
        form.fields['message'].queryset = Message.objects.filter(owner=user)
        return form

    def form_valid(self, form):
        mailing = form.save()
        user = self.request.user
        mailing.owner = user
        mailing.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if not user.is_superuser and user != self.object.owner:
            raise PermissionDenied
        return self.object


class MailingUpdateView(LoginRequiredMixin, UpdateView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        user = self.request.user
        if user == self.object.owner or user.is_superuser:
            form.fields['send_to'].queryset = Client.objects.filter(owner=user)
            form.fields['message'].queryset = Message.objects.filter(owner=user)
        return form

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return MailingForm
        elif user.has_perm('mailing.set_activation_mailing'):
            return MailingManagerForm
        raise PermissionDenied


class MailingDetailView(LoginRequiredMixin, DetailView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Mailing


class MailingDeleteView(LoginRequiredMixin, DeleteView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        user = self.request.user
        if user == self.object.owner:
            return context_data
        raise PermissionDenied


class ClientListView(LoginRequiredMixin, ListView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Client

    def get_queryset(self):
        user = self.request.user
        return Client.objects.filter(owner=user)


class ClientCreateView(LoginRequiredMixin, CreateView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')

    def form_valid(self, form):
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ClientForm
        raise PermissionDenied


class ClientDetailView(LoginRequiredMixin, DetailView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Client


class ClientDeleteView(LoginRequiredMixin, DeleteView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Client
    success_url = reverse_lazy('mailing:client_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        user = self.request.user
        if user == self.object.owner:
            return context_data
        raise PermissionDenied


class MessageListView(LoginRequiredMixin, ListView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Message

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(owner=user)


class MessageCreateView(LoginRequiredMixin, CreateView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')

    def form_valid(self, form):
        message = form.save()
        user = self.request.user
        message.owner = user
        message.save()
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Message
    fields = ('theme', 'body',)
    success_url = reverse_lazy('mailing:message_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return MessageForm
        raise PermissionDenied


class MessageDetailView(LoginRequiredMixin, DetailView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Message


class MessageDeleteView(LoginRequiredMixin, DeleteView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = Message
    success_url = reverse_lazy('mailing:message_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        user = self.request.user
        if user == self.object.owner:
            return context_data
        raise PermissionDenied


class MailingLogListView(LoginRequiredMixin, ListView):

    login_url = "/users/login/"
    redirect_field_name = "/users/login/"

    model = MailingLog
