from django.http import HttpResponse
from django.shortcuts import render
from .constants import POSTS, MENU


def main_page(request):
    data = {"menu": MENU, "posts": POSTS}
    return render(request, './main.html', context=data)


def post_page(request, id):
    post = POSTS[id]
    data = {"menu": MENU, "post": post}
    return render(request, './post.html', context=data)


def about_page(request):
    title = "О блоге"
    data = {"menu": MENU, "title": title}
    return render(request, './about.html', context=data)
