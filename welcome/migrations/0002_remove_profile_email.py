# Generated by Django 2.0.2 on 2018-03-07 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]
