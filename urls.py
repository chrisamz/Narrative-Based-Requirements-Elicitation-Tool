from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:project_id>/update/', views.project_update, name='project_update'),
    path('projects/<int:project_id>/delete/', views.project_delete, name='project_delete'),
    
    path('projects/<int:project_id>/stories/create/', views.story_create, name='story_create'),
    path('projects/<int:project_id>/stories/<int:story_id>/update/', views.story_update, name='story_update'),
    path('projects/<int:project_id>/stories/<int:story_id>/delete/', views.story_delete, name='story_delete'),
    
    path('projects/<int:project_id>/requirements/create/', views.requirement_create, name='requirement_create'),
    path('projects/<int:project_id>/requirements/<int:requirement_id>/update/', views.requirement_update, name='requirement_update'),
    path('projects/<int:project_id>/requirements/<int:requirement_id>/delete/', views.requirement_delete, name='requirement_delete'),
    
    path('projects/<int:project_id>/relationships/create/', views.relationship_create, name='relationship_create'),
    path('projects/<int:project_id>/relationships/<int:relationship_id>/update/', views.relationship_update, name='relationship_update'),
    path('projects/<int:project_id>/relationships/<int:relationship_id>/delete/', views.relationship_delete, name='relationship_delete'),
    
    path('projects/<int:project_id>/visualize/', views.visualize_requirements, name='visualize_requirements'),
]
