from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .templates.forms import Create_task, Create_project
# Create your views here.

def hello(request):
    return render(request, 'index.html')

def prueba(request, id):
    return HttpResponse("Esto es una prueba y contiene " + str(id))

def projects(request):
    return render(request, 'projects/show.html', {
        'projects': Project.objects.all()
    })

def projectDetails(request, id):
    return render(request, 'projects/show.html', {
        'project': get_object_or_404(Project, id=id)
    })

def tasks(request):
    return render(request, 'tasks/show.html', {
        'tasks': Task.objects.all()
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create.html', {
            'form': Create_task()
        })
    else:
        Task.objects.create(project_id=1,title=request.POST['title'], description=request.POST['description'])
        return redirect('tasks')
    

def create_project(request):
    print("Entra")
    if request.method == 'GET':
        return render(request, 'projects/create.html', {
            'form': Create_project()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')