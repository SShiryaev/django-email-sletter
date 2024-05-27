from django.db import models
# from django.utils import timezone
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    """Модель клиента сервиса. Ему будет приходить рассылка."""

    email = models.EmailField(max_length=30, unique=True, verbose_name='почта')
    name = models.CharField(max_length=50, verbose_name='ФИО')
    comment = models.TextField(max_length=500, **NULLABLE, verbose_name='комментарий')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Message(models.Model):
    """Модель сообщения для рассылки."""

    theme = models.CharField(max_length=100, verbose_name='тема')
    body = models.TextField(max_length=500, verbose_name='содержание')

    def __str__(self):
        return f'Сообщение по теме: {self.theme}\nТекст: {self.body}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Mailing(models.Model):
    """
    Модель рассылки.
    Рассылка внутри себя содержит ссылки на модели «Сообщение» и «Клиент сервиса».
    Сообщение у рассылки может быть только одно, а клиентов может быть много.
    """

    class Periodicity(models.TextChoices):
        PER_A_DAY = "Раз в день", _("Раз в день")
        PER_A_WEEK = "Раз в неделю", _("Раз в неделю")
        PER_A_MONTH = "Раз в месяц", _("Раз в месяц")

    class Status(models.TextChoices):
        CREATED = "Создана", _("Создана")
        LAUNCHED = "Запущена", _("Запущена")
        FINISHED = "Завершена", _("Завершена")
    # PERIODICITY_MAILING = [
    #     ('once_day', 'раз в день'),
    #     ('once_week', 'раз в неделю'),
    #     ('once_month', 'раз в месяц'),
    # ]
    #
    # STATUS_MAILING = [
    #     ('created', 'создана'),
    #     ('launched', 'запущена'),
    #     ('completed', 'завершена')
    # ]

    name = models.CharField(max_length=50, verbose_name='название')
    send_at = models.DateTimeField(**NULLABLE, verbose_name='первая отправка')
    periodicity = models.CharField(max_length=20, choices=Periodicity, verbose_name='периодичность')
    status = models.CharField(max_length=20, choices=Status, verbose_name='статус')
    send_to = models.ManyToManyField(Client, verbose_name='получатель')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, **NULLABLE, verbose_name='сообщение')

    def __str__(self):
        return f'Рассылка с названием: {self.name}, получатель: {self.send_to}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class MailingLog(models.Model):
    """
    Попытка рассылки. У одной рассылки может быть много попыток,
    но одна попытка относится только к одной конкретной рассылке.
    """

    last_try = models.DateTimeField(**NULLABLE, verbose_name='последняя попытка')
    mailing_status = models.BooleanField(default=False, verbose_name='успешно')
    post_log = models.CharField(max_length=200, **NULLABLE, verbose_name='ответ почтового сервиса')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка')

    def __str__(self):
        return f'Статус: {self.mailing_status}, дата попытки: ({self.last_try})'

    class Meta:
        verbose_name = 'лог рассылки'
        verbose_name_plural = 'логи рассылок'
