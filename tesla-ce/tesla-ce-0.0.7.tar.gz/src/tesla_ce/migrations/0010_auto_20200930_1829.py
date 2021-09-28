# Generated by Django 3.0 on 2020-09-30 16:29

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('tesla_ce', '0009_monitor'),
    ]

    operations = [
        migrations.AddField(
            model_name='institutionuser',
            name='inst_admin',
            field=models.BooleanField(default=False, help_text='Whether this user is administrator of the institution'),
        ),
        migrations.AddField(
            model_name='institutionuser',
            name='legal_admin',
            field=models.BooleanField(default=False, help_text='Whether this user can manage legal data of the institution'),
        ),
        migrations.AddField(
            model_name='institutionuser',
            name='send_admin',
            field=models.BooleanField(default=False, help_text='Whether this user can manage SEND data of the institution'),
        ),
    ]
