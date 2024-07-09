from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import pprint
import json
from newsapi import NewsApiClient
import requests

# Create your views here.
url = "https://newsapi.org/v2/top-headlines"
newsapi = NewsApiClient(api_key='b1e128f1633c4c27bbb274fe7b73cec3')
@login_required    
def events_page(request):
    return render(request,"blogTemplates/events.html")

@login_required
def news_page(request, category=None):
    if category:
        top_headlines = newsapi.get_top_headlines(category=category, language='en', country='in')
    else:
        top_headlines = newsapi.get_top_headlines(language='en', country='in')

    articles = top_headlines.get("articles")
    return render(request, "blogTemplates/news.html", {
        "username": request.user.username,
        "articles": articles
    })

@login_required
def home_page(request):
    # response = requests.get(url,params={
    #     "country":"in",
    #     "category":"business",
    #     "apiKey":apiKey
    # })
    all_articles = newsapi.get_everything(q='general',language='en',sort_by='publishedAt',page=2)    
    articles = all_articles.get("articles")
    return render(request, "blogTemplates/news.html", {
        "username":request.user.username,
        "articles":articles
    })