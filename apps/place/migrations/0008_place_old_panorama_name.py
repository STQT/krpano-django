# Generated by Django 5.0.4 on 2024-04-14 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0007_alter_place_panorama'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='old_panorama_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
