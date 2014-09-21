from django import template
from django.template.loader import get_template
from django.core.urlresolvers import reverse

from xcblog.models import BlogCategory, BlogPost

register = template.Library()

class BlogCategoryList(template.Node):
    def render(self, context):
        categories = BlogCategory.objects.all()
        t = get_template('xcblog/category_list.html')
        output = t.render(template.Context({'categories': categories}))
        return output

@register.tag()
def category_list(parser, token):
    return BlogCategoryList()

class BlogArchiveList(template.Node):
    def render(self, context):
        archives = BlogPost.objects.datetimes('created_time', 'month')
        output_archives = [{'year': d.year, 'month': d.month, 'month2': '%02d' % d.month} for d in archives]
        t = get_template('xcblog/archive_list.html')
        output = t.render(template.Context({'archives': output_archives}))
        return output

@register.tag()
def archive_list(parser, token):
    return BlogArchiveList()
