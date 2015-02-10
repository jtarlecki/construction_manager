# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0004_auto_20150203_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materials',
            name='createddate',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendors',
            name='website',
            field=models.URLField(max_length=2000, blank=True),
            preserve_default=True,
        ),
    ]
