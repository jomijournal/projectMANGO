from django.shortcuts import render
from django.http import HttpResponse


def all_articles(request):
    return HttpResponse("Hello!")

def articles_by_subject(request, article_id):
    return HttpResponse("Hi!")
