# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('work_evid', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='created')),
                ('todo', models.TextField(verbose_name='todo', blank=True)),
                ('firm', models.ForeignKey(verbose_name='firma', to='work_evid.Firm')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
