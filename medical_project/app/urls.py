from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup_view,name="signup"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('dashboard/',views.dashboard_view,name="dashboard"),
    path('create_blog_post/', views.create_blog_post, name='create_blog_post'),
    path('view_blog_posts/', views.view_blog_posts, name='view_blog_posts'),
    path('api/blog-posts/', views.blog_posts_api_view, name='blog_posts_api'),
]
