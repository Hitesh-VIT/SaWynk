# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='playlist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Artist', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=500)),
                ('genre', models.CharField(max_length=500)),
                ('album', models.CharField(max_length=500)),
                ('link', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='playlist',
            name='song',
            field=models.ForeignKey(to='song.Songs'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
