from django.shortcuts import get_object_or_404, render, HttpResponse
from .models import Project
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa

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


def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


def resumeView(request):

    pdf = render_to_pdf('resume/resume.html')
    return HttpResponse(pdf, content_type='application/pdf')