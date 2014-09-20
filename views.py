from django.shortcuts import get_object_or_404, render
from xcblog.models import BlogCategory, BlogPost

def homepage(request):
    blogposts = BlogPost.objects.filter(is_active=True)
    context = {
        'title': '首页',
        'blogposts': blogposts,
    }
    return render(request, 'xcblog/homepage.html', context)

def show_blogpost(request, pk):
    blogpost = get_object_or_404(BlogPost, pk=pk)
    if blogpost.is_active == False:
        context = {
            'title': '博主暂时不打算公开这篇日志',
        }
        return render(request, 'xcblog/not_active.html', context)
    else:
        blogpost.read_times += 1
        blogpost.save(update_fields=['read_times'])
        context = {
            'title': blogpost.title,
            'b': blogpost,
        }
        return render(request, 'xcblog/show_blogpost.html', context)

def show_category(request, pk):
    category = get_object_or_404(BlogCategory, pk=pk)
    blogposts = BlogPost.objects.filter(is_active=True, category=category)
    context = {
        'title': category.name,
        'c': category,
        'blogposts': blogposts,
    }
    return render(request, 'xcblog/show_category.html', context)
