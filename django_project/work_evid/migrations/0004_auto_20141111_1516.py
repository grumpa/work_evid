# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work_evid', '0003_auto_20141027_1519'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['finished', '-date']},
        ),
        migrations.AlterField(
            model_name='todo',
            name='finished',
            field=models.BooleanField(default=False, verbose_name='finished'),
        ),
    ]
