# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('work_evid', '0004_auto_20141111_1516'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='firm',
            options={'ordering': ['name'], 'verbose_name': 'firm'},
        ),
        migrations.AlterField(
            model_name='firm',
            name='description',
            field=models.TextField(verbose_name='description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='firm',
            name='from_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='from date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='firm',
            name='name',
            field=models.CharField(max_length=60, verbose_name='firm name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='firm',
            name='periode',
            field=models.IntegerField(default=1, help_text='How often we make an invoice.', verbose_name='periode [months]'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='todo',
            name='firm',
            field=models.ForeignKey(verbose_name='firm', to='work_evid.Firm'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='work',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='work date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='work',
            name='firm',
            field=models.ForeignKey(verbose_name='firm', to='work_evid.Firm'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='work',
            name='item_price',
            field=models.DecimalField(verbose_name='price for item', max_digits=15, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='work',
            name='items',
            field=models.DecimalField(default=1, verbose_name='ammount of items', max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='work',
            name='what_brief',
            field=models.CharField(max_length=80, verbose_name='what (briefly)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='work',
            name='what_detailed',
            field=models.TextField(verbose_name='describe detailed', blank=True),
            preserve_default=True,
        ),
    ]
