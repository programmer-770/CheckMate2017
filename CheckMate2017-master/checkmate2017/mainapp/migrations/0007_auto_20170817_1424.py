# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-17 08:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20170817_1420'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Buildings',
            new_name='Building',
        ),
        migrations.RenameModel(
            old_name='GameSwitches',
            new_name='GameSwitch',
        ),
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
    ]
