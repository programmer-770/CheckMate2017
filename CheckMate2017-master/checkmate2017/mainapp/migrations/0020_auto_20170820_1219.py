# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-20 06:49
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_auto_20170820_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='phone2',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email2',
            field=models.CharField(blank=True, help_text='The email id should be in this format: f201xxxxx@pilani.bits-pilani.ac.in', max_length=34, null=True, validators=[django.core.validators.RegexValidator(re.compile('^f201[0-9]{4-5}@pilani\\.bits-pilani\\.ac\\.in$', 32), 'Enter yor valid BITS-mail', 'invalid!')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='idno1',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(re.compile('^201[0-9]{1}[0-9][A-Z]{4}[0-9]{4}P$', 32), 'Enter your valid BITS-mail', 'invalid!')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='idno2',
            field=models.CharField(max_length=20, null=True, validators=[django.core.validators.RegexValidator(re.compile('^201[0-9]{1}[0-9][A-Z]{4}[0-9]{4}P$', 32), 'Enter your valid BITS-mail', 'invalid!')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone1',
            field=models.BigIntegerField(null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d{10}$', 32), 'Enter the valid phone number.', 'Invalid!')]),
        ),
    ]
