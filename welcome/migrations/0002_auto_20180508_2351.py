# Generated by Django 2.0.2 on 2018-05-08 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatar_image'),
        ),
        migrations.AddField(
            model_name='profile',
            name='insta',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
