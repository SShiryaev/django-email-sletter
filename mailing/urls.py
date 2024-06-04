from django.urls import path
from django.views.decorators.cache import never_cache, cache_page
from mailing.apps import MailingConfig
from mailing.views import (IndexView, MailingListView, MailingCreateView, MailingUpdateView, MailingDetailView,
                           MailingDeleteView, ClientListView, ClientCreateView, ClientUpdateView, ClientDetailView,
                           ClientDeleteView, MessageListView, MessageCreateView, MessageUpdateView, MessageDetailView,
                           MessageDeleteView, MailingLogListView)

app_name = MailingConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('mailing_list/', never_cache(MailingListView.as_view()), name='mailing_list'),
    path('mailing_create/', never_cache(MailingCreateView.as_view()), name='mailing_create'),
    path('mailing_update/<int:pk>/', never_cache(MailingUpdateView.as_view()), name='mailing_update'),
    path('mailing_detail/<int:pk>/', never_cache(MailingDetailView.as_view()), name='mailing_detail'),
    path('mailing_delete/<int:pk>/', never_cache(MailingDeleteView.as_view()), name='mailing_delete'),

    path('client_list/', never_cache(ClientListView.as_view()), name='client_list'),
    path('client_create/', never_cache(ClientCreateView.as_view()), name='client_create'),
    path('client_update/<int:pk>/', never_cache(ClientUpdateView.as_view()), name='client_update'),
    path('client_detail/<int:pk>/', never_cache(ClientDetailView.as_view()), name='client_detail'),
    path('client_delete/<int:pk>/', never_cache(ClientDeleteView.as_view()), name='client_delete'),

    path('message_list/', never_cache(MessageListView.as_view()), name='message_list'),
    path('message_create/', never_cache(MessageCreateView.as_view()), name='message_create'),
    path('message_update/<int:pk>/', never_cache(MessageUpdateView.as_view()), name='message_update'),
    path('message_detail/<int:pk>/', never_cache(MessageDetailView.as_view()), name='message_detail'),
    path('message_delete/<int:pk>/', never_cache(MessageDeleteView.as_view()), name='message_delete'),

    path('mailinglog_list/', never_cache(MailingLogListView.as_view()), name='mailinglog_list'),
]
