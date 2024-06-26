# Generated by Django 5.0.2 on 2024-02-21 20:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Giornaliero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('descrizione', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Dettagli',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movimento', models.CharField(choices=[('TABACCHI', 'TABACCHI'), ('LOTTO', 'LOTTO'), ('ART. TABACCHERIA', 'ART. TABACCHERIA'), ('SISAL', 'SISAL'), ('GRATTA E VINCI', 'GRATTA E VINCI'), ('ALTRE USCITE', 'ALTRE USCITE'), ('PASTIGLIAGGI', 'PASTIGLIAGGI'), ('VALORI BOLLATI', 'VALORI BOLLATI')], max_length=100)),
                ('entrata', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('uscita', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('giornaliero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='statistiche.giornaliero')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('giornaliero', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='statistiche.giornaliero')),
            ],
        ),
    ]
