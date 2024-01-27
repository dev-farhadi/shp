# Generated by Django 5.0.1 on 2024-01-27 10:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category_Object',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Type_Object',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='object',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1080)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category_object')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.type_object')),
            ],
        ),
    ]
