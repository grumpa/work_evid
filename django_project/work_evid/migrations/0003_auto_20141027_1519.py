# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work_evid', '0002_todo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='todo',
            name='finished',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
