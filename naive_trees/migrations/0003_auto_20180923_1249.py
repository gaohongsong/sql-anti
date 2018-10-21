# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app_mtpp', '0002_mpttfood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mpttfood',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', blank=True, to='app_mtpp.MpttFood', null=True),
        ),
        migrations.AlterField(
            model_name='mpttfood',
            name='title',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
