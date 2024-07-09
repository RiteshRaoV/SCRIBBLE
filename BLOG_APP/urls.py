from django.urls import path

from BLOG_APP import views


urlpatterns = [
    path('add-blogs/',views.add_blogs_page,name='events'),
    path('news/', views.news_page, name='news'),
    path('news/<str:category>/', views.news_page, name='news_category'),
    path('home/',views.home_page,name='home'),
    path('user-blogs/',views.get_user_blogs,name='user_blogs')

]
