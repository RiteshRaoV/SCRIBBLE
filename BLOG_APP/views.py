from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from newsapi import NewsApiClient
from .models import Blog
from django.core import serializers
from django.contrib.auth import get_user_model
# Create your views here.
url = "https://newsapi.org/v2/top-headlines"
newsapi = NewsApiClient(api_key="b1e128f1633c4c27bbb274fe7b73cec3")

User = get_user_model()
def is_superuser(user):
    return user.is_authenticated and user.is_superuser

@login_required
def add_blogs_page(request):
    if request.method == "POST":
        blog_type = request.POST.get("category")
        blog_title = request.POST.get("title")
        blog_content = request.POST.get("content")
        if not blog_type or not blog_title or not blog_content:
            return render(request, "blogTemplates/add_blog.html",{
                "message":"Something Went wrong!!"
            })

        blog = Blog(
            user=request.user,
            blog_type=blog_type,
            blog_title=blog_title,
            blog_content=blog_content,
            status="Pending",
        )
        blog.save()

        return render(request, "blogTemplates/add_blog.html",{
                "message":"Blog Submitted!!"
            }) 

    return render(request, "blogTemplates/add_blog.html")

@login_required
@user_passes_test(is_superuser)
def all_blogs(request):
    users = User.objects.filter(blogs= not None).distinct()
    return render(request,"blogTemplates/allBlogs.html",{
        "users":users
    })

@login_required
@user_passes_test(is_superuser)
def change_blog_status(request):
    if request.method=="POST":
        blog_id = request.POST.get("blog_id")
        blog_status = request.POST.get("status")
        
        blog = Blog.objects.get(pk=blog_id)
        blog.status = blog_status
        blog.save()
        
        return redirect("all_blogs")

def get_user_blogs(request):
    user = request.user
    user_blogs = user.blogs.all()
    return render(request,"blogTemplates/user_blogs.html",{
        "blogs":user_blogs
    })


@login_required
def news_page(request, category="general"):
    if category:
        top_headlines = newsapi.get_top_headlines(
            category=category, language="en", country="in"
        )
    else:
        top_headlines = newsapi.get_top_headlines(language="en", country="in")

    articles = top_headlines.get("articles")
    return render(
        request,
        "blogTemplates/news.html",
        {"username": request.user.username, "articles": articles},
    )


@login_required
def home_page(request):
    # response = requests.get(url,params={
    #     "country":"in",
    #     "category":"business",
    #     "apiKey":apiKey
    # })
    all_articles = newsapi.get_everything(
        q="general", language="en", sort_by="publishedAt", page=2
    )
    articles = all_articles.get("articles")
    return render(
        request,
        "blogTemplates/news.html",
        {"username": request.user.username, "articles": articles},
    )
