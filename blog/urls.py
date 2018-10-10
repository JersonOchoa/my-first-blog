from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.listar,name = 'listar'),
        url(r'^post/(?P<pk>[0-9]+)/$', views.detalle,  name='detalle'),
        url(r'^post/new/$', views.post_new, name='post_new'),
        url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]
