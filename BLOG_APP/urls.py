from django.urls import path

from BLOG_APP import views


urlpatterns = [
    path('add-blogs/',views.add_blogs_page,name='add_blogs'),
    path('news/', views.news_page, name='news'),
    path('news/<str:category>/', views.news_page, name='news_category'),
    path('home/',views.home_page,name='home'),
    path('all-blogs/',views.all_blogs,name='all_blogs'),
    path('update-blog-status/',views.change_blog_status,name='change_blog_status'),
    path('blogs/',views.blog_display,name='approved_blogs')

]
