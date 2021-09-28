# Generated by Django 3.1.12 on 2021-06-03 16:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lti_consumer", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="lticonsumer",
            name="inline_ratio",
            field=models.FloatField(
                blank=True,
                default=0.5625,
                validators=[
                    django.core.validators.MinValueValidator(0.1),
                    django.core.validators.MaxValueValidator(10),
                ],
            ),
        ),
        migrations.AddField(
            model_name="lticonsumer",
            name="is_automatic_resizing",
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name="lticonsumer",
            name="lti_provider_id",
            field=models.CharField(
                blank=True,
                choices=[
                    (None, "Custom provider configuration"),
                    ("lti_provider_test", "LTI Provider Test Video"),
                ],
                help_text="Please choose a predefined provider or fill fields below.",
                max_length=50,
                null=True,
                verbose_name="Predefined LTI provider",
            ),
        ),
    ]
