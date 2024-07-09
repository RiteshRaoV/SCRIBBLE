from django.urls import path

from BLOG_APP import views


urlpatterns = [
    path('events/',views.events_page,name='events'),
    path('news/', views.news_page, name='news'),
    path('news/<str:category>/', views.news_page, name='news_category'),
    path('home/',views.home_page,name='home')
]