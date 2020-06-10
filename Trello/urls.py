"""Trello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from trelloApp.views.logs import SigninView, SignupView, logout_view
from trelloApp.views.board import HomeView
from trelloApp.views.board import BoardView, create_project, delete_all_project, BoardAPIViewSet


from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'boardAPI', BoardAPIViewSet, basename='boardAPI')


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'logout/', logout_view, name='logout'),
    url(r'^connexion', SigninView.as_view(), name='signin'),
    path('inscription/', SignupView.as_view(), name='signup'),
    path('', HomeView.as_view(), name='home'),
    url(r'board/(?P<project_id>\d+)/$', BoardView.as_view(), name='board'),
    path('delete_all_project/', delete_all_project, name='delete_all-project'),
    path('ajax_create_project/', create_project, name='create_project'),
    url(r'^api/', include(router.urls)),
]
