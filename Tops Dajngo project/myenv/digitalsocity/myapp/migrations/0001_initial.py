# Generated by Django 5.0 on 2024-01-04 05:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Chairman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('contect', models.CharField(max_length=11)),
                ('blockno', models.CharField(max_length=3)),
                ('houseno', models.CharField(max_length=4)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
