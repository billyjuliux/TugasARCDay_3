"""todo URL Configuration

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
from django.contrib import admin
from django.urls import path
from todoapp.views import home, delete, cross, uncross, edit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('delete/<int:list_id>/', delete),
    path('cross/<int:list_id>/', cross),
    path('uncross/<int:list_id>/', uncross),
    path('edit/<int:list_id>/', edit)
]
