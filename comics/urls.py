from django.urls import path
from . import views

urlpatterns = [
    path('', views.comics_list, name='comics_list'),
    path('comic/<int:comic_id>/', views.comic_detail, name='comic_detail'),
]