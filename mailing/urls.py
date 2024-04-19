from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import (IndexView, MailingListView, MailingCreateView, MailingUpdateView, MailingDetailView,
                           MailingDeleteView)

app_name = MailingConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('mailing_list/', MailingListView.as_view(), name='mailing_list'),
    path('mailing_create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing_update/<int:pk>/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing_detail/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing_delete/<int:pk>/', MailingDeleteView.as_view(), name='mailing_delete'),
]
