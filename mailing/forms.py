from django import forms
from django.core.exceptions import ValidationError
from users.forms import StyleFormMixin

from mailing.models import Client, Mailing, Message


class ProductForm(StyleFormMixin, forms.ModelForm):
    """Форма добавления/изменения клиента"""

    class Meta:
        model = Client
        fields = ('email', 'name', 'comment',)


# class ProductModeratorForm(StyleFormMixin, forms.ModelForm):
#     """Форма добавления/изменения продукта СЗР для модератора"""
#
#     class Meta:
#         model = Product
#         fields = ('is_published', 'description', 'category',)
#
#
# class VersionForm(StyleFormMixin, forms.ModelForm):
#     """Форма добавления/изменения версии продукта
#     в данном случае номера гос. регистрации/окончания регистрации в РФ
#     """
#
#     class Meta:
#         model = Version
#         fields = '__all__'

    # def clean_is_current(self):
    #     cleaned_data = self.cleaned_data.get('is_current')
    #     current_version = Version.objects.filter(is_current=self.cleaned_data.get('is_current')).distinct()
    #     if cleaned_data and current_version:
    #         raise ValidationError('Актуальная версия может быть одна, снимите флаг с предыдущей')
    #     return cleaned_data


# class FeedbackForm(StyleFormMixin, forms.ModelForm):
#     """Форма добавления контактных данных клиента"""
#
#     class Meta:
#         model = Feedback
#         fields = '__all__'