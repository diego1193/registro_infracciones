# Generated by Django 5.0.1 on 2024-01-25 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Infraccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa_patente', models.CharField(max_length=10)),
                ('timestamp', models.DateTimeField()),
                ('comentarios', models.TextField()),
            ],
        ),
    ]
