from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('aboutme/', views.aboutme_view, name='aboutme'),
    path('group/', views.group_view, name='group'),
    path('how/', views.how_view, name='how'),
    path('individual/', views.individual_view, name='individual'),
]