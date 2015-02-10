# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0006_auto_20150203_2138'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employees',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='jobs',
            options={'ordering': ['createddate']},
        ),
        migrations.AlterModelOptions(
            name='materials',
            options={'ordering': ['date']},
        ),
        migrations.AlterModelOptions(
            name='vendors',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='jobs',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='materials',
            name='receipt_number',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='modifieduser',
            field=models.CharField(default=b'admin', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='employees',
            name='modifieduser',
            field=models.CharField(default=b'admin', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='employees',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'(\\d{3})\\D*(\\d{3})\\D*(\\d{4})$', message=b"Phone number must be entered in the format: '800-555-1212'")]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jobphases',
            name='createduser',
            field=models.CharField(default=b'admin', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jobphases',
            name='modifieduser',
            field=models.CharField(default=b'admin', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jobs',
            name='createduser',
            field=models.CharField(default=b'admin', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jobs',
            name='modifieduser',
            field=models.CharField(default=b'admin', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='materials',
            name='createduser',
            field=models.CharField(default=b'admin', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='materials',
            name='modifieduser',
            field=models.CharField(default=b'admin', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendors',
            name='createduser',
            field=models.CharField(default=b'admin', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendors',
            name='modifieduser',
            field=models.CharField(default=b'admin', max_length=50),
            preserve_default=True,
        ),
    ]
