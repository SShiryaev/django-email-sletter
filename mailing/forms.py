from django import forms
from django.core.exceptions import ValidationError
from users.forms import StyleFormMixin

from mailing.models import Client, Mailing, Message


class ClientForm(StyleFormMixin, forms.ModelForm):
    """Форма добавления/изменения клиента"""

    class Meta:
        model = Client
        exclude = ('owner',)


class MailingForm(StyleFormMixin, forms.ModelForm):
    """Форма добавления/изменения рассылки"""

    class Meta:
        model = Mailing
        fields = ('name', 'send_at', 'periodicity', 'send_to', 'message',)


class MailingManagerForm(StyleFormMixin, forms.ModelForm):
    """Форма изменения рассылки менеджера"""

    class Meta:
        model = Mailing
        fields = ('status',)


class MessageForm(StyleFormMixin, forms.ModelForm):
    """Форма добавления/изменения сообщения рассылки"""

    class Meta:
        model = Message
        exclude = ('owner',)


# class FeedbackForm(StyleFormMixin, forms.ModelForm):
#     """Форма добавления контактных данных клиента"""
#
#     class Meta:
#         model = Feedback
#         fields = '__all__'
