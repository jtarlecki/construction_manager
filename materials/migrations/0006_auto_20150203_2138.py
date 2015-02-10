# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0005_auto_20150203_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='materials',
            name='date',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='materials',
            name='createddate',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
