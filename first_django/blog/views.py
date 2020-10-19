from django.shortcuts import render
from .models import Post
from django.http.response import JsonResponse
# Create your views here.
'''
posts=[
    {
        'author':'vimal',
        'Content':"first post content",
        'title':"first post"
    }
    ,
    {
        'author':'viren',
        'Content':"second post content",
        'title':"second post"
    }
    ,
    {
        'author':'vijay',
        'Content':"third post content",
        'title':"third post"
    }

]
'''

def view_json_post(request):
    posts = Post.objects.all().values();
    post_list=list(posts);
    return JsonResponse({'data':post_list});

def view_post(request):
    posts= Post.objects.all()

    return render(request,"blog/index.html")

