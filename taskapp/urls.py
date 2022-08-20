from . import views
from django.urls import path

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('delete/<str:pk>/', views.delete_post, name="delete"),
    path('update/<str:pk>/', views.update_post, name="update"),
    path('search/', views.searchNote, name="search"),   
]
