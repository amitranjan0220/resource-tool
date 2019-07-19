from django.urls import path
from  . import views

urlpatterns = [
    path('home', views.resource_home, name="resource_home"),
    path('add_resource', views.add_resource, name="add_resource"),
    path('add_category', views.add_category, name="add_category"),
    path('view_resource', views.view_resource, name="view_resource"),
    path('view_resource/<int:item_id>/', views.all_resource, name="all_resource"),
    path('all_item/', views.all_item, name="all_item"),
    path('edit_item/<int:item_id>/', views.edit_item, name="edit_item"),
    path('delete_resource/<int:item_id>/', views.delete_resource, name="delete_resource"),
    path('download_csv/', views.download_csv, name="download_csv"),
]