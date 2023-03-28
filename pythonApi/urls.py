"""pythonApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings #for image
from django.conf.urls.static import static #for image upload
from pythonApi import views
from pythonApi import auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', views.posts_list),
    path('add_post/', views.add_post),
    path('post/<int:pk>', views.getpost),
    path('delete/<int:pk>', views.deletepost),
    path('edit/<int:pk>', views.editpost),
    path('search/', views.search),
    path('register/', auth.register),
    path('login', auth.login),
    path('profile/<str:email>', auth.profile)
]

# for image upload
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)