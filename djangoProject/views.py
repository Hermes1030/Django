# from django.http import response
from django.shortcuts import render


def home(request):
    # return response.HttpResponse("This is my first page and this is the home of the project.")
    return render(request, 'home.html')


def about(request):
    # return response.HttpResponse("About me in this project.")
    return render(request, 'about.html')
