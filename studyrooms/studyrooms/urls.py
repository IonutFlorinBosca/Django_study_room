"""
URL configuration for studyrooms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import path, include

# my core url's file
# I will be using 2 url files, one for the root, one for the app
# to create a view, I am gonna use function based views

# in a big project it will be very messy to have both the views and the
# urls in the same file
# the views will be added to the app's views file

# I will be creating a url's file that will contain all the urls for the app
# this will contain just the paths for the app

# with the help of include, django will take care of all the core url routing
# for the base app
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
]
