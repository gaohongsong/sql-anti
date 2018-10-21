# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('parent', models.ForeignKey(related_name='children', blank=True, to='naive_trees.Food', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MpttFood',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=50)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('mptt_level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='naive_trees.MpttFood', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
