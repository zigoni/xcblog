# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xcblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='名称')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('order', models.IntegerField(default=0, help_text='只能输入整数', verbose_name='顺序')),
                ('blogpost_num', models.PositiveIntegerField(default=0, verbose_name='文章数')),
            ],
            options={
                'verbose_name_plural': '分类',
                'verbose_name': '分类',
                'ordering': ['order', '-created_time'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ForeignKey(default=1, to='xcblog.BlogCategory'),
            preserve_default=True,
        ),
    ]
