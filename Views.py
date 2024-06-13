# app/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import Project, Story, Requirement, Relationship
from .forms import ProjectForm, StoryForm, RequirementForm, RelationshipForm

@login_required
def project_list(request):
    projects = Project.objects.filter(members=request.user)
    return render(request, 'app/project_list.html', {'projects': projects})

@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id, members=request.user)
    stories = project.stories.all()
    requirements = project.requirements.all()
    relationships = project.relationships.all()
    return render(request, 'app/project_detail.html', {
        'project': project,
        'stories': stories,
        'requirements': requirements,
        'relationships': relationships
    })

@login_required
@require_http_methods(["GET", "POST"])
def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            project.members.add(request.user)
            return redirect('project_detail', project_id=project.id)
    else:
        form = ProjectForm()
    return render(request, 'app/project_form.html', {'form': form})

@login_required
@require_http_methods(["GET", "POST"])
def project_update(request, project_id):
    project = get_object_or_404(Project, id=project_id, owner=request.user)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'app/project_form.html', {'form': form})

@login_required
@require_http_methods(["POST"])
def project_delete(request, project_id):
    project = get_object_or_404(Project, id=project_id, owner=request.user)
    project.delete()
    return redirect('project_list')

@login_required
@require_http_methods(["GET", "POST"])
def story_create(request, project_id):
    project = get_object_or_404(Project, id=project_id, members=request.user)
    if request.method == "POST":
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.user = request.user
            story.project = project
            story.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = StoryForm()
    return render(request, 'app/story_form.html', {'form': form, 'project': project})

@login_required
@require_http_methods(["GET", "POST"])
def story_update(request, project_id, story_id):
    project = get_object_or_404(Project, id=project_id, members=request.user)
    story = get_object_or_404(Story, id=story_id, project=project, user=request.user)
    if request.method == "POST":
        form = StoryForm(request.POST, instance=story)
        if form.is_valid():
            form.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = StoryForm(instance=story)
    return render(request, 'app/story_form.html', {'form': form, 'project': project})

@login_required
@require_http_methods(["POST"])
def story_delete(request, project_id, story_id):
    project = get_object_or_404(Project, id=project_id, members=request.user)
    story = get_object_or_404(Story, id=story_id, project=project, user=request.user)
    story.delete()
    return redirect('project_detail', project_id=project.id)

@login_required
@require_http_methods(["GET", "POST"])
def requirement_create(request, project_id):
    project = get_object_or_404(Project, id=project_id, members=request.user)
    if request.method == "POST":
        form = RequirementForm(request.POST)
        if form.is_valid():
            requirement = form.save(commit=False)
            requirement.project = project
            requirement.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = RequirementForm()
    return render(request, 'app/requirement_form.html', {'form': form, 'project': project})

@login_required
@require_http_methods(["GET", "POST"])
def requirement_update(request, project_id, requirement_id):
    project = get_object_or_404(Project, id=project_id, members=request.user)
    requirement = get_object_or_404(Requirement, id=requirement_id, project=project)
    if request.method == "POST":
        form = RequirementForm(request.POST, instance=requirement)
        if form.is_valid():
            form.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = RequirementForm(instance=requirement)
    return render(request, 'app/requirement_form.html', {'form': form, 'project': project})

@login_required
@require_http_methods(["POST"])
def requirement_delete(request, project_id, requirement_id):
    project = get_object_or_404(Project, id=project_id, members=request.user)
    requirement = get_object_or_404(Requirement, id=requirement_id, project=project)
    requirement.delete()
    return redirect('project_detail', project_id=project.id)

@login_required
@require_http_methods(["GET", "POST"])
def relationship_create(request, project_id):
    project = get_object_or_404(Project, id=project_id, members=request.user)
    if request.method == "POST":
        form = RelationshipForm(request.POST)
        if form.is_valid():
            relationship = form.save(commit=False)
            relationship.project = project
            relationship.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = RelationshipForm()
    return render(request, 'app/relationship_form.html', {'form': form, 'project': project})

@login_required
@require_http_methods(["GET", "POST"])
def relationship_update(request, project_id, relationship_id):
    project = get_object_or_404(Project, id=project_id, members=request.user)
    relationship = get_object_or_404(Relationship, id=relationship_id, project=project)
    if request.method == "POST":
        form = RelationshipForm(request.POST, instance=relationship)
        if form is_valid():
            form.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = RelationshipForm(instance=relationship)
    return render(request, 'app/relationship_form.html', {'form': form, 'project': project})

@login_required
@require_http_methods(["POST"])
def relationship_delete(request, project_id, relationship_id):
    project = get_object_or_404(Project, id=project_id, members=request.user)
    relationship = get_object_or_404(Relationship, id=relationship_id, project=project)
    relationship.delete()
    return redirect('project_detail', project_id=project.id)

@login_required
def visualize_requirements(request, project_id):
    project = get_object_or_404(Project, id=project_id, members=request.user)
    requirements = project.requirements.all()
    relationships = project.relationships.all()
    # Add visualization logic here
    return render(request, 'app/visualize_requirements.html', {'project': project, 'requirements': requirements, 'relationships': relationships})
