# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 05:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning_blogs_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Infa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_blogs_app.Topic')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]