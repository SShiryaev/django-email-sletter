# Generated by Django 5.0.3 on 2024-04-20 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0008_rename_mailingstatus_mailinglog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailinglog',
            options={'verbose_name': 'лог рассылки', 'verbose_name_plural': 'логи рассылок'},
        ),
    ]