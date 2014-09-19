from django.shortcuts import render
from xcblog.models import BlogPost

def homepage(request):
    blogposts = BlogPost.objects.filter(is_active=True)
    context = {
        'title': '首页',
        'blogposts': blogposts,
    }
    return render(request, 'xcblog/homepage.html', context)

def show_blogpost(request, pk):
    blogpost = BlogPost.objects.get(pk=pk)
    if blogpost.is_active == False:
        context = {
            'title': '博主暂时不打算公开这篇日志',
        }
        return render(request, 'xcblog/not_active.html', context)
    else:
        blogpost.read_times += 1
        blogpost.save()
        context = {
            'title': blogpost.title,
            'blogpost': blogpost,
        }
        return render(request, 'xcblog/show_blogpost.html', context)
