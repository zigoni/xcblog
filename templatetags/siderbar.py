from django import template
from django.template.loader import get_template
from django.core.urlresolvers import reverse

from xcblog.models import BlogCategory

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