# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Firm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60, verbose_name='jm\xe9no firmy')),
                ('periode', models.IntegerField(default=1, help_text='Jak \u010dasto fakturujeme.', verbose_name='perioda [m\u011bs\xedce]')),
                ('from_date', models.DateField(default=django.utils.timezone.now, verbose_name='od data')),
                ('description', models.TextField(verbose_name='popis', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'firma',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='datum pr\xe1ce')),
                ('item_price', models.DecimalField(verbose_name='cena za jednotku', max_digits=15, decimal_places=2)),
                ('items', models.DecimalField(default=1, verbose_name='mno\u017estv\xed jednotek', max_digits=10, decimal_places=2)),
                ('what_brief', models.CharField(max_length=80, verbose_name='co (stru\u010dn\u011b)')),
                ('what_detailed', models.TextField(verbose_name='detailn\xed popis', blank=True)),
                ('firm', models.ForeignKey(verbose_name='firma', to='work_evid.Firm')),
            ],
            options={
                'ordering': ['-date'],
            },
            bases=(models.Model,),
        ),
    ]
