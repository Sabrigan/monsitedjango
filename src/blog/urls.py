from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bio', views.bio, name='bio'),
    url(r'^projets', views.projets, name='projets'),
    url(r'^competences', views.competences, name='competences'),
    url(r'^experiences', views.experiences, name='experiences'),
    url(r'^informatique', views.informatique, name='informatique'),
    url(r'^autre', views.autre, name='autre'),

    url(r'^post/(?P<id>[0-9]+)$', views.show, name='show'),

]
