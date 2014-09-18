from django.shortcuts import render
from xcblog.models import BlogPost

def homepage(request):
    blogposts = BlogPost.objects.filter(is_active=True)
    context = {
        'title': '首页',
        'blogposts': blogposts,
    }
    return render(request, 'xcblog/homepage.html', context)