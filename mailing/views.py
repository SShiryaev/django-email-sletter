from django.views.generic import TemplateView, ListView
from mailing.models import Mailing


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
