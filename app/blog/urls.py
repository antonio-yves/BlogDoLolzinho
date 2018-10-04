from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views as blog

app_name = 'blog'

urlpatterns = [
	path('', blog.Home.as_view(), name = 'home'),
	path('champion/<pk>/detail', blog.ChampionView.as_view(), name = 'champion-detail'),
	path('champions/', blog.ChampionsView.as_view(), name = 'champions'),
	path('news/', blog.NewsView.as_view(), name = 'news'),
	path('search/', blog.ResultsView.as_view(), name = 'search'),
	path('post/<pk>', blog.NewsDetail.as_view(), name = 'news-detail'),
	path('about/', blog.About.as_view(), name = 'about'),
	path('contact/', blog.Contact.as_view(), name = 'contact'),
]