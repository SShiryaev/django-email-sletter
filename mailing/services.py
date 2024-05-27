from datetime import datetime, timedelta

import pytz
from django.core.mail import send_mail

from config import settings
from mailing.models import Mailing, MailingLog, Message


# def change_status(mailing, time) -> None:
#     if mailing.mailing_status == 'Создана':
#         mailing.mailing_status = 'started'
#         print('started')
#     elif mailing.mailing_status == 'started' and mailing.stop_datetime_mailing <= time:
#         mailing.mailing_status = 'finished'
#         print('finished')
#     mailing.save()


# def send_mailing():
#     zone = pytz.timezone(settings.TIME_ZONE)
#     current_datetime = datetime.now(zone)
#     # создание объекта с применением фильтра
#
#     mailings = Mailing.objects.filter(send_at__lte=current_datetime, status__in=[Mailing.Status])
#
#     for mailing in mailings:
#         try:
#             send_mail(
#                     subject=mailing.message.theme,
#                     # message=Message.objects.get(id=mailing.id).body,
#                     message=mailing.message.body,
#                     from_email=settings.EMAIL_HOST_USER,
#                     recipient_list=[send_to.email for send_to in mailing.send_to.all()]
#             )
#             if (
#                     mailing.periodicity == Mailing.periodicity.PER_A_DAY
#                     and current_datetime.day >= 1
#             ):
#                 mailing.send_at = F("sent_time") + timedelta(days=1)
#                 mailing.status = MailingSettings.StatusMailingSettings.STARTED
#             elif (
#                     mailing.period == MailingSettings.PeriodMailingSettings.ONE_WEEK
#                     and current_datetime.day >= 7
#             ):
#                 mailing.sent_time = F("sent_time") + timedelta(days=7)
#                 mailing.status = MailingSettings.StatusMailingSettings.STARTED
#             elif (
#                     mailing.period == MailingSettings.PeriodMailingSettings.ONE_MONTH
#                     and current_datetime.day >= 30
#             ):
#                 mailing.sent_time = F("sent_time") + timedelta(days=30)
#                 mailing.status = MailingSettings.StatusMailingSettings.STARTED
#                 mailing.save()
#                 status = True
#                 server_response = "успешно"
#         except smtplib.SMTPResponseException as e:
#             status = False
#             server_response = str(e)
#
#         finally:
#             Logs.objects.create(
#             mailing=mailing,
#             status=status,
#             server_response=server_response,
#         )
#             log = MailingLog.objects.create(mailing_status=send_mail, mailing=mailing)
#             log.save()
#
#         except Exception as SendMailingError:
#             log = MailingLog.objects.create(mailing_status=send_mail, mailing=mailing, post_log=SendMailingError)
#             log.save()
