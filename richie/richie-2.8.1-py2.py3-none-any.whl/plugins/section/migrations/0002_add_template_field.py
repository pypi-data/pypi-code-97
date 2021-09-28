# Generated by Django 2.1.7 on 2019-02-22 01:57

from django.db import migrations, models

from ..defaults import SECTION_TEMPLATES


class Migration(migrations.Migration):

    dependencies = [("section", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="section",
            name="template",
            field=models.CharField(
                choices=SECTION_TEMPLATES,
                default=SECTION_TEMPLATES[0][0],
                help_text="Optional template for custom look.",
                max_length=150,
                verbose_name="Template",
            ),
        )
    ]
