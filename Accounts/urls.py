"""ClinicalTrial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.template.defaulttags import url
from django.urls import path, re_path
from Accounts import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('userlist/', views.UserListView.as_view(), name='userlist'),
    re_path(r'^password/$', views.Change_password.as_view(), name='change_password'),
    #path('change_password/', views.ChangePassword.as_view(), name='change_password'),
    path('register/user_perm/<int:id>/', views.UserPermSetting.as_view()),
]