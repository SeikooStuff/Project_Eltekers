# Generated by Django 5.0.4 on 2025-06-04 07:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web_eltekers", "0003_alter_instruktur_sasana_alter_peserta_sasana"),
    ]

    operations = [
        migrations.AlterField(
            model_name="instruktur",
            name="sasana",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="instrukturs",
                to="web_eltekers.sasana",
            ),
        ),
        migrations.AlterField(
            model_name="peserta",
            name="sasana",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pesertas",
                to="web_eltekers.sasana",
            ),
        ),
    ]
