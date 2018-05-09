# Generated by Django 2.0.2 on 2018-05-09 12:54

import awesome_avatar.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0004_auto_20180509_0141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=awesome_avatar.fields.AvatarField(upload_to='avatars'),
        ),
    ]