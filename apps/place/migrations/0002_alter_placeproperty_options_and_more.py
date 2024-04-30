# Generated by Django 5.0.4 on 2024-04-13 23:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='placeproperty',
            options={'verbose_name': 'место пропертй', 'verbose_name_plural': 'место пропертй'},
        ),
        migrations.AlterField(
            model_name='placeproperty',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='place.place', verbose_name='место'),
        ),
        migrations.AlterField(
            model_name='placeproperty',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='place.property', verbose_name='пропертй'),
        ),
    ]
