# Generated by Django 2.0.2 on 2018-03-07 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('vk', models.CharField(blank=True, max_length=50)),
                ('telegram', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
