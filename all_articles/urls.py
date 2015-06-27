from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.all_articles, name='all_articles'),
    url(r'^(?P<subject>[a-z\-]+)$', views.articles_by_subject, name='articles_by_subjects'),
]