# Generated by Django 4.1 on 2023-03-30 09:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='image/')),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]