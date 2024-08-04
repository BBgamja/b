"""
URL configuration for config project.

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
from django.urls import path, include

from firstapp import views as f_views
from mainapp import views as m_views
from secondapp import views as s_views

# urlpatterns = [
#     path('index/', f_views.getIndexPage),
#     path('index/', f_views.getIndexPage2),
#     path('index3/', m_views.getIndexPage),
#     path('index4/', s_views.getIndexPage),
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
    path('first/', include('firstapp.urls')),

    path('', m_views.getIndexPage),
]
