from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name="index"),
    path('prueba/<int:id>', views.prueba, name="prueba"),
    path('projects', views.projects, name="projects"),
    path('projects/<int:id>', views.projectDetails, name="projectsDetails"),
    path('tasks', views.tasks, name="tasks"),
    path('create/task', views.create_task, name="create_task"),
    path('create/project', views.create_project, name="create_project"),
]