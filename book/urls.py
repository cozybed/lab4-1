__author__ = 'yousihan'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$',views.login),
    url(r'^login/saveNewBook$',views.save),
    url(r'^search$',views.search),
    url(r'^books$',views.single),
    url(r'^edit',views.edit),
    url(r'^delete',views.delete),
    url(r'^login/saveNewAuthor',views.saveNewAuthor)
]
