from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('grid/', views.grid, name='grid'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('post/', views.single_post, name='single_post'),
    path('blog/pagina-2/', views.blog_page_2, name='blog_page_2'),
]



