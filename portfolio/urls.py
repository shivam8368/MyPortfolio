from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolioPageView , name = "portfolio"),
    path('<int:id>', views.projectPageView , name = "project"),
]