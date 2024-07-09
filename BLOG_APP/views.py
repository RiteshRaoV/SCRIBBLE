from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from newsapi import NewsApiClient
from .models import Blog
from django.core import serializers

# Create your views here.
url = "https://newsapi.org/v2/top-headlines"
newsapi = NewsApiClient(api_key="b1e128f1633c4c27bbb274fe7b73cec3")


@login_required
def add_blogs_page(request):
    if request.method == "POST":
        blog_type = request.POST.get("castegory")
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
            status="pending",
        )
        blog.save()

        return redirect("events") 

    return render(request, "blogTemplates/add_blog.html")


def get_user_blogs(request):
    user = request.user
    user_blogs = user.blogs.all()
    data = serializers.serialize('json', user_blogs)  
    return render(request,"blogTemplates/user_blogs.html",{
        "blogs":user_blogs
    })
    return JsonResponse({'blogs': data}, safe=False)


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
