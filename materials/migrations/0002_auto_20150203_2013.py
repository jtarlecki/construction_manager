# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vendors',
            options={'ordering': ['pk']},
        ),
        migrations.AddField(
            model_name='materials',
            name='comments',
            field=models.TextField(default=datetime.datetime(2015, 2, 4, 1, 13, 29, 124000, tzinfo=utc), max_length=5000),
            preserve_default=False,
        ),
    ]
