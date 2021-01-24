from django.db import models

# Create your models here.


class Project(models.Model):

    name = models.CharField(max_length=200)
    discription = models.CharField(max_length=800)
    detail_discription = models.TextField()

    project_url = models.URLField(max_length=500)
    project_github_url = models.URLField(max_length=800)

    tech_used_one = models.CharField(max_length = 200, blank=True)
    tech_used_two = models.CharField(max_length = 200, blank=True)
    tech_used_three = models.CharField(max_length = 200, blank=True)
    tech_used_four = models.CharField(max_length = 200, blank=True)
    tech_used_five = models.CharField(max_length = 200, blank=True)
    tech_used_six = models.CharField(max_length = 200, blank=True)


    # images

    project_main_image = models.ImageField(upload_to='media/projects/%Y/%m/', blank=True)
    project_ss_one = models.ImageField(upload_to='media/projects/%Y/%m/', blank=True)
    project_ss_two = models.ImageField(upload_to='media/projects/%Y/%m/', blank=True)
    project_ss_three = models.ImageField(upload_to='media/projects/%Y/%m/', blank=True)
    project_ss_four = models.ImageField(upload_to='media/projects/%Y/%m/', blank=True)
    project_ss_five = models.ImageField(upload_to='media/projects/%Y/%m/', blank=True)
    project_ss_six = models.ImageField(upload_to='media/projects/%Y/%m/', blank=True)


    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name