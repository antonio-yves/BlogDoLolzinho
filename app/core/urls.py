from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views as core

app_name = 'core'

urlpatterns = [
	path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	#path('cadastro/', core.UserCreateView.as_view(), name='cadastro'),
]