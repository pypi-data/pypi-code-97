# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-30 05:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painless_redirects', '0002_auto_20170803_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redirect',
            name='domain',
            field=models.CharField(blank=True, default='', help_text='Optional, exlicitly limit to specific domain.', max_length=64),
        ),
    ]
