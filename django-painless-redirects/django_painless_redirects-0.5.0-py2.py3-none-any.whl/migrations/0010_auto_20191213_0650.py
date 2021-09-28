# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-13 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painless_redirects', '0009_redirect_enabled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redirect',
            name='enabled',
            field=models.BooleanField(default=True, help_text='Shall this redirect be effectivly used?', verbose_name='Enabled'),
        ),
    ]
