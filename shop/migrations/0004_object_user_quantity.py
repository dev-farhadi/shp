# Generated by Django 5.0.1 on 2024-01-28 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_object_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='object_user',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]