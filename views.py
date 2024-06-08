from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Project
from home.forms import ProjectForm

# Create your views here.

class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        projects = Project.objects.all()
        context = {'project_list': projects}
        return render(request, "home/main.html", context)

class ProjectCreateView(View):
    def get(self, request):
        form = ProjectForm()
        context = {"form": form}
        return render(request, "home/project_forms.html", context)

    def post(self, request):
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("all"))

        context = {"form": form}
        return render(request, "home/project_form.html", context)

class ProjectDetailView(View):
    def get(self, request, project_id):
        project = get_object_or_404(Project, pk=project_id)
        context = {'project': project}
        return render(request, 'home/project_detail.html', context)

class ProjectEditView(View):
    def get(self, request, project_id):
        project = get_object_or_404(Project, pk=project_id)
        form = ProjectForm(instance=project)
        context = {"form": form, "project": project}
        return render(request, "home/project_edit.html", context)

    def post(self, request, project_id):
        project = get_object_or_404(Project, pk=project_id)
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("all"))
        context = {"form": form, "project": project}
        return render(request, "home/project_edit.html", context)

class ProjectDeleteView(View):
    def get(self, request, project_id):
        project = get_object_or_404(Project, pk=project_id)
        context = {'project': project}
        return render(request, "home/project_delete.html", context)

    def post(self, request, project_id):
        project = get_object_or_404(Project, pk=project_id)
        project.delete()
        return HttpResponseRedirect(reverse("all"))

