#coding: utf-8

from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class BlogCategory(models.Model):
    name = models.CharField('名称', max_length=10)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    order = models.IntegerField('顺序', help_text='只能输入整数', default=0)
    blogpost_num = models.PositiveIntegerField('文章数', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'
        ordering = ['order', '-created_time']

class BlogPost(models.Model):
    title = models.CharField('标题', max_length=128)
    is_active = models.BooleanField('是否可见', default=True)
    category = models.ForeignKey(BlogCategory, default=1)
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

@receiver(post_save, sender=BlogPost)
def increase_blogpost_num(sender, instance, created, **kwargs):
    if created:
        blogcategory = instance.category
        blogcategory.blogpost_num += 1
        blogcategory.save()
    else:
        pass

@receiver(post_delete, sender=BlogPost)
def decrease_blogpost_num(sender, instance, **kwargs):
    blogcategory = instance.category
    blogcategory.blogpost_num -= 1
    blogcategory.save()
