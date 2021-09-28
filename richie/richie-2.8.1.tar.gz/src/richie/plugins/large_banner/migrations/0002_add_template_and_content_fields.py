# Generated by Django 2.1.7 on 2019-02-21 01:18

from django.db import migrations, models

from ..defaults import LARGEBANNER_TEMPLATES


class Migration(migrations.Migration):

    dependencies = [("large_banner", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="largebanner",
            name="content",
            field=models.TextField(blank=True, default="", verbose_name="Content"),
        ),
        migrations.AddField(
            model_name="largebanner",
            name="template",
            field=models.CharField(
                choices=LARGEBANNER_TEMPLATES,
                default=LARGEBANNER_TEMPLATES[0][0],
                help_text="Choose template to render plugin.",
                max_length=150,
                verbose_name="Template",
            ),
        ),
    ]
