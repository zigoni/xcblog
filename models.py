#coding: utf-8

from django.db import models

class BlogPost(models.Model):
    title = models.CharField('标题', max_length=128)
    is_active = models.BooleanField('是否可见', default=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    revised_time = models.DateTimeField('修改时间', auto_now=True)
    read_times = models.PositiveIntegerField('阅读次数', default=0)
    content = models.TextField(u'内容', max_length=5000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '日志'
        verbose_name_plural = '日志'
        ordering = ['-created_time']
