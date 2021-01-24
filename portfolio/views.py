from django.shortcuts import get_object_or_404, render
from .models import Project

# Create your views here.


def portfolioPageView(request):
    projects = Project.objects.order_by('created_at')

    data = {
        'projects': projects,
    }


    return render(request, 'webpages/portfolio/portfolio.html', data)





def projectPageView(request , id):

    project = get_object_or_404(Project , pk=id)
    
    data = {
        'project' : project
    }

    return render(request, 'webpages/projects/project.html', data)