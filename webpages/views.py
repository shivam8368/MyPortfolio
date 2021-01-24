from django.shortcuts import render
from .models import Contact

# Create your views here.


def homePageView(request):
    return render(request, 'webpages/home/home.html')




def aboutPageView(request):

    if request.method == 'POST':
        name = request.POST['contactName']
        email = request.POST['contactEmail']
        subject = request.POST['contactSubject']
        message = request.POST['contactMessage']


        contact = Contact(name=name , email = email , subject=subject, message=message)
        contact.save()

    return render(request, 'webpages/about/about.html')