# Generated by Django 3.0.8 on 2020-07-21 08:22

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('tesla_ce', '0007_auto_20200712_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestproviderresult',
            name='result',
            field=models.FloatField(default=0.0, help_text='Normalized result value', null=True),
        ),
        migrations.AlterField(
            model_name='requestresult',
            name='result',
            field=models.FloatField(default=0.0, help_text='Normalized result value, summarizing results from providers', null=True),
        ),
    ]
