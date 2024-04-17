from django.contrib import admin
from mailing.models import Client, Message, Mailing, MailingStatus


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'comment')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('theme', 'body')


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('send_at', 'periodicity', 'status', 'message')


@admin.register(MailingStatus)
class MailingStatusAdmin(admin.ModelAdmin):
    list_display = ('last_try', 'mailing_status', 'post_log', 'mailing')
