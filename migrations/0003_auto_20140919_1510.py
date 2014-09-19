# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xcblog', '0002_auto_20140919_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.ForeignKey(default=1, to='xcblog.BlogCategory'),
        ),
    ]
