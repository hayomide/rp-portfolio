from django.shortcuts import render
from projects.models import Project

def project_index(request):
    # query to retriev all object in the project table
    projects = Project.objects.all()   
    # dictionary context to store all object from the query
    context = {'projects' : projects }
    return render(request, "project_index.html", context) 

def project_detail(request, pk):
    project = Project.objects.get(pk=pk) #query retrieving the project with the primary key
    context = {'project' : project }
    return render(request, "project_detail.html", context)

# Create your views here.
