from django.db import models
# from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    """Модель клиента сервиса. Ему будет приходить рассылка."""

    email = models.EmailField(max_length=30, unique=True, verbose_name='почта')
    name = models.CharField(max_length=50, verbose_name='ФИО')
    comment = models.TextField(max_length=500, **NULLABLE, verbose_name='комментарий')

    def __str__(self):
        return f'{self.email} ({self.name})'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Message(models.Model):
    """Модель сообщения для рассылки."""

    theme = models.CharField(max_length=100, verbose_name='тема')
    body = models.TextField(max_length=500, verbose_name='содержание')

    def __str__(self):
        return f'Сообщение по теме: {self.theme}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Mailing(models.Model):
    """Модель рассылки.
    Рассылка внутри себя содержит ссылки на модели «Сообщение» и «Клиент сервиса».
    Сообщение у рассылки может быть только одно, а клиентов может быть много.
    """

    PERIODICITY_MAILING = [
        ('once_day', 'раз в день'),
        ('once_week', 'раз в неделю'),
        ('once_month', 'раз в месяц'),
    ]

    STATUS_MAILING = [
        ('created', 'создана'),
        ('launched', 'запущена'),
        ('completed', 'завершена')
    ]

    send_at = models.DateTimeField(**NULLABLE, verbose_name='первая отправка')
    periodicity = models.CharField(max_length=10, choices=PERIODICITY_MAILING, verbose_name='периодичность')
    status = models.CharField(max_length=9, choices=STATUS_MAILING, verbose_name='статус')
    send_to = models.ManyToManyField(Client, verbose_name='получатель')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, **NULLABLE, verbose_name='сообщение')

    def __str__(self):
        return f'Рассылка со статусом: {self.status}, периодичность: {self.periodicity}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class MailingStatus(models.Model):
    """Попытка рассылки. У одной рассылки может быть много попыток,
    но одна попытка относится только к одной конкретной рассылке.
    """

    last_try = models.DateTimeField(**NULLABLE, verbose_name='последняя попытка')
    mailing_status = models.BooleanField(default=False, verbose_name='успешно')
    post_log = models.CharField(max_length=200, **NULLABLE, verbose_name='ответ почтового сервиса')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка')

    def __str__(self):
        return f'Статус: {self.mailing_status}, дата попытки: ({self.last_try})'

    class Meta:
        verbose_name = 'статус рассылки'
        verbose_name_plural = 'статусы рассылок'
