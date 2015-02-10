# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_auto_20150203_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='password',
            field=models.CharField(default=datetime.datetime(2015, 2, 4, 1, 26, 50, 899000, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employees',
            name='username',
            field=models.CharField(default='fix', unique=True, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendors',
            name='location',
            field=models.CharField(max_length=1000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='createduser',
            field=models.CharField(default=b'admin', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='modifieduser',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='employees',
            name='createduser',
            field=models.CharField(default=b'admin', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='employees',
            name='modifieduser',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
