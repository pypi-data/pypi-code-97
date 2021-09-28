# Generated by Django 3.1 on 2020-09-12 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpme', '0006_auto_20200911_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_type',
            field=models.IntegerField(choices=[(0, 'Message'), (1, 'Event')], default=0, verbose_name='Type'),
        ),
    ]
