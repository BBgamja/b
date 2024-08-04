from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.getIndexPage),
    path('index2/', views.getIndexPage2),
]

