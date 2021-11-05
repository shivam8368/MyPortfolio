from django.contrib import admin
from .models import Project
from django.utils.html import format_html

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):

    def projectImage(self, object):
        return format_html('<img src="{}" width="40">'.format(object.project_main_image.url))

    list_display = ('name', 'projectImage', 'discription')

admin.site.register(Project , ProjectAdmin)
