from django.shortcuts import render
from django.http import HttpResponse


def all_articles(request):
    return HttpResponse("Hello!")

def article(request, article_id):
    return HttpResponse("Hi!")

def article_with_name(request, article_id, article_name):
    return HttpResponse("Amazing!")