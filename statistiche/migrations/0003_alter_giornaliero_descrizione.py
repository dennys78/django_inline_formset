# Generated by Django 5.0.2 on 2024-03-06 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistiche', '0002_giornaliero_differenza_giornaliero_incassopresunto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giornaliero',
            name='descrizione',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
