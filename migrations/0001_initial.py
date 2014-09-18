# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128, verbose_name='标题')),
                ('is_active', models.BooleanField(verbose_name='是否可见', default=True)),
                ('created_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('revised_time', models.DateTimeField(verbose_name='修改时间', auto_now=True)),
                ('read_times', models.PositiveIntegerField(verbose_name='阅读次数', default=0)),
                ('content', models.TextField(max_length=5000, verbose_name='内容')),
            ],
            options={
                'verbose_name': '日志',
                'verbose_name_plural': '日志',
                'ordering': ['-created_time'],
            },
            bases=(models.Model,),
        ),
    ]
