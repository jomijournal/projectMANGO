from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.template import RequestContext, loader

from .models import Article

def all_articles(request):
    return HttpResponseRedirect('/articles/')

def article(request, articleID):
    try:
        article = Article.objects.get(articleID=articleID)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    return render(request, 'journal/article.html', {'article': article})


def article_with_name(request, articleID, articleName):
    return article(request, articleID)