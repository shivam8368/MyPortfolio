from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolioPageView , name = "portfolio"),
    path('resume/', views.resumeView , name = "resume"),
    path('<int:id>', views.projectPageView , name = "project"),
]