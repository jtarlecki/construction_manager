# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('owner', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('address1', models.CharField(max_length=500, blank=True)),
                ('address2', models.CharField(max_length=500, blank=True)),
                ('city', models.CharField(max_length=500, blank=True)),
                ('state', models.CharField(max_length=500, blank=True)),
                ('zipcode', models.CharField(max_length=5, blank=True)),
                ('email', models.EmailField(max_length=75)),
                ('website', models.URLField(max_length=2000)),
                ('createduser', models.CharField(max_length=50)),
                ('createddate', models.DateField(auto_now_add=True)),
                ('modifieduser', models.CharField(default=b'admin', max_length=50)),
                ('modifieddate', models.DateField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('initials', models.CharField(max_length=5)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('address1', models.CharField(max_length=500, blank=True)),
                ('address2', models.CharField(max_length=500, blank=True)),
                ('city', models.CharField(max_length=500, blank=True)),
                ('state', models.CharField(max_length=500, blank=True)),
                ('zipcode', models.CharField(max_length=5, blank=True)),
                ('email', models.EmailField(max_length=75)),
                ('createduser', models.CharField(max_length=50)),
                ('createddate', models.DateField(auto_now_add=True)),
                ('modifieduser', models.CharField(default=b'admin', max_length=50)),
                ('modifieddate', models.DateField(auto_now=True)),
                ('company', models.ForeignKey(to='materials.Company')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobPhases',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jobphase', models.CharField(max_length=1000)),
                ('createduser', models.CharField(max_length=50)),
                ('createddate', models.DateField(auto_now_add=True)),
                ('modifieduser', models.CharField(max_length=50)),
                ('modifieddate', models.DateField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1000)),
                ('est_start_date', models.DateField(auto_now_add=True)),
                ('start_date', models.DateField()),
                ('est_end_date', models.DateField()),
                ('end_date', models.DateField()),
                ('createduser', models.CharField(max_length=50)),
                ('createddate', models.DateField(auto_now_add=True)),
                ('modifieduser', models.CharField(max_length=50)),
                ('modifieddate', models.DateField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(max_digits=15, decimal_places=2)),
                ('createduser', models.CharField(max_length=50)),
                ('createddate', models.DateField(auto_now_add=True)),
                ('modifieduser', models.CharField(max_length=50)),
                ('modifieddate', models.DateField(auto_now=True)),
                ('job', models.ForeignKey(to='materials.Jobs')),
                ('phase', models.ForeignKey(to='materials.JobPhases')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1000)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('address1', models.CharField(max_length=500, blank=True)),
                ('address2', models.CharField(max_length=500, blank=True)),
                ('city', models.CharField(max_length=500, blank=True)),
                ('state', models.CharField(max_length=500, blank=True)),
                ('zipcode', models.CharField(max_length=5, blank=True)),
                ('email', models.EmailField(max_length=75)),
                ('website', models.URLField(max_length=2000)),
                ('createduser', models.CharField(max_length=50)),
                ('createddate', models.DateField(auto_now_add=True)),
                ('modifieduser', models.CharField(max_length=50)),
                ('modifieddate', models.DateField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='materials',
            name='vendor',
            field=models.ForeignKey(to='materials.Vendors'),
            preserve_default=True,
        ),
    ]
