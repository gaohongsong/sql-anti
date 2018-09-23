# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_mtpp', '0003_auto_20180923_1249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mpttfood',
            old_name='level',
            new_name='mptt_level',
        ),
    ]
