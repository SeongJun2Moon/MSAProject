"""admin URL Configuration

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
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from admin.views import hello

urlpatterns = [
    path('', hello),
    path("blog/auth/", include('blog.busers.urls')),
    path("movies/movies/", include('movies.musers.urls')),
    path("stroke/", include("blog.stroke.urls")),
    path("shop/iris/", include("shop.iris.urls")),
    path("shop/fashion", include("shop.fashion.urls")),
    path("shop/number", include("shop.number.url")),
    path("webcrawler", include("webcrawler.urls")),
]
