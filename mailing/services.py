from datetime import datetime, timedelta
import smtplib

import pytz
from django.core.mail import send_mail

from config import settings
from mailing.models import Mailing, MailingLog


def change_mailing_status(mailing):
    dict_periodicity = {
        'Раз в день': 0,
        'Еженедельно': 7,
        'Ежемесячно': 30
    }
    periodicity = dict_periodicity[mailing.periodicity]
    if periodicity == 0:
        mailing.status = mailing.Status.FINISHED
    else:
        mailing_last = mailing.sent_time + timedelta(days=periodicity)
        if mailing_last > mailing.data_mailing_finish:
            mailing.status = mailing.Status.FINISHED
        else:
            mailing.sent_time = mailing_last
            mailing.status = mailing.Status.LAUNCHED
    mailing.save()


def create_log_mailings(mailing, current_datetime, log, server):

    MailingLog.objects.create(
        mailing=mailing,
        datatime=current_datetime,
        status=log,
        answer_mail_server=server,
    )


def send_mailing():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    # создание объекта с применением фильтра

    mailings = Mailing.objects.filter(send_at__lte=current_datetime, status__in=[Mailing.Status.CREATED, Mailing.Status.LAUNCHED])

    for mailing in mailings:
        subject = mailing.message.theme
        message = mailing.message.body
        clients = mailing.send_to.all()
        for client in clients:
            try:
                log_server = send_mail(
                            subject=subject,
                            message=message,
                            from_email=settings.EMAIL_HOST_USER,
                            recipient_list=[client.email]
                )
                log_status = MailingLog.mailing_status is True
            except smtplib.SMTPResponseException as error:
                log_server = str(error)
                log_status = MailingLog.mailing_status is False
            finally:
                create_log_mailings(mailing, current_datetime, log_status, log_server)

            change_mailing_status(mailing)



