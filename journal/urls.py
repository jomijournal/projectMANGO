from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.all_articles, name = "all_articles"),
    url(r'^(?P<article_id>[0-9]+)$', views.article, name = "article"),
    url(r'^(?P<article_id>[0-9]+)/(?P<article_name>[a-z\-]+)$',
        views.article_with_name, name = "article_with_name"),
]
