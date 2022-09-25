from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('string-match-percentage', views.stringMatchPercentage, name='string-match-percentage'),
]