# Generated by Django 2.0.2 on 2018-05-16 05:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='avatars')),
                ('description', models.CharField(blank=True, max_length=100)),
                ('vk', models.CharField(blank=True, max_length=50)),
                ('telegram', models.CharField(blank=True, max_length=50)),
                ('whatsapp', models.CharField(blank=True, max_length=50)),
                ('viber', models.CharField(blank=True, max_length=50)),
                ('insta', models.CharField(blank=True, max_length=50)),
                ('skype', models.CharField(blank=True, max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
