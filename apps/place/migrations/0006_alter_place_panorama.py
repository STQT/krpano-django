# Generated by Django 5.0.4 on 2024-04-14 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0005_place_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='panorama',
            field=models.ImageField(blank=True, null=True, upload_to='upload_panorama', verbose_name='панорама'),
        ),
    ]
