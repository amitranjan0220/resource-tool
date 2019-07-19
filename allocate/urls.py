from django.urls import path
from . import views

urlpatterns = [
    path('allocate_home/', views.allocate_home, name='allocate_home'),
    path('allocate_resource/', views.allocate_resource, name='allocate_resource'),
    path('allocate_view/', views.allocate_view, name='allocate_view'),
    path('search_by_user/', views.search_by_user, name='search_by_user'),
    path('search_by_resource/', views.search_by_resource, name='search_by_resource'),
    path('ajax_load_resource/', views.load_resources, name="ajax_load_resource"),
    path('select_resource/<int:pk>/', views.select_resource, name="select_resource")
 
]