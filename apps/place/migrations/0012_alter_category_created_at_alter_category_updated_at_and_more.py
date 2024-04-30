# Generated by Django 5.0.4 on 2024-04-14 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0011_category_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='создано'),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='обновленное время'),
        ),
        migrations.AlterField(
            model_name='place',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='создано'),
        ),
        migrations.AlterField(
            model_name='place',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='обновленное время'),
        ),
        migrations.AlterField(
            model_name='property',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='создано'),
        ),
        migrations.AlterField(
            model_name='property',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='обновленное время'),
        ),
    ]
