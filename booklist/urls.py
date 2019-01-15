"""booklist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include

from my_booklist.views import *


urlpatterns = [
    path('', BookCreateView.as_view(), name='index'),
    #path('search/', BookSearch, name='search'),
    path('isbn/', isbn_search, name='isbn'),
    path('detail/<int:pk>/', DetailView.as_view(), name='detail'),
    path('detail/<int:pk>/rent/', RentNow, name='rent'),
    path('return/', ReturnBooksView.as_view(), name='return_view'),
    path('return/<int:pk>', ReturnNow, name='return_now'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), #認証関連
    path('accounts/', include('accounts.urls')), #サインアップ
]
