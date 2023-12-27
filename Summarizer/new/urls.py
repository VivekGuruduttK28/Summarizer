"""new URL Configuration

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
from django.contrib import admin
from django.urls import path
from app_name import views
from .settings import MEDIA_ROOT,MEDIA_URL
from django.conf.urls.static import static
from django.urls import include, path
from django.urls import path

from django.conf.urls import handler404

handler404 = views.error_404

urlpatterns = [
    path('land/<str:uname>',views.landing),
    path('summarize1/<str:uname>',views.index),
    path('pay',views.pay),
    path('summarize2/<str:uname>',views.summarize2),
    path('',views.login),
    path('iot/<str:uname>',views.tot),
    path('subscribe/<str:uname>',views.pay),
    path('signup',views.signup),
    path('signin',views.signin),
    path('stt/<str:uname>',views.stt),
    path('payment/<str:uname>',views.payment),
    path('audio/<str:uname>',views.audio),
    path('makeittrue/<str:uname>',views.makeittrue),
]+ static(MEDIA_URL, document_root=MEDIA_ROOT)
