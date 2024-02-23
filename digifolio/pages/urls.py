from django.urls import path
from pages import views

urlpatterns = [
    path("home/", views.home, name='home'),
    path("details/", views.project_index, name="project_index"),
    path('new/', views.newProject, name='NewGroup'),
    path("list/", views.project_list, name="project_list"),
]