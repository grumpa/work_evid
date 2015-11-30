# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_evid', '0005_auto_20150203_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='firm',
            name='show_in_list',
            field=models.BooleanField(default=True, verbose_name='show in list'),
        ),
    ]
