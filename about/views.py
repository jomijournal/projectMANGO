from django.shortcuts import render

def home(request):
    return (request, 'about/base.html')
