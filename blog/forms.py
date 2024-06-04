from django import forms

from users.forms import StyleFormMixin
from blog.models import Material


class MaterialForm(StyleFormMixin, forms.ModelForm):
    """Форма добавления/изменения статьи"""

    class Meta:
        model = Material
        fields = ('title', 'body', 'preview',)
