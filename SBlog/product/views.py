import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Post


# Create your views here.

def index(request):
    return HttpResponse('Home Page')


def post_list(request):
    # return HttpResponse('Post Page')
    posts = Post.PublishManager.all()
    context = {'posts': posts}
    return render(request, "product/list.html", context)


def post_detail(request, id):
    # return HttpResponse('Post Detail')
    # try:
    #     post = Post.PublishManager.get(id=id)
    # except:
    # raise Http404('Post not found')
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)

    context = {
        'post': post,
        'new_date': datetime.datetime.now()
    }
    return render(request, "product/detail.html", context)
