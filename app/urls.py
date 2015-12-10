from django.conf.urls import include, url
from app import views

urlpatterns = [
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r'^sites', views.sites, name='sites'),
    url(r'^site/(?P<pk>[0-9]+)/$', views.site, name='site'),
    url(r'^site/new/$', views.site_new, name='site_new'),
    url(r'^site/(?P<pk>[0-9]+)/edit/$', views.site_edit, name='site_edit'),
    url(r'^site/(?P<pk>[0-9]+)/edit/site_delete$', views.client_delete, name='site_delete'),
    #url(r'^test_admin/$', 'app.views.test_admin', name='test_admin'),
    
    url(r'^clients', views.clients, name='clients'),
    url(r'^client/(?P<pk>[0-9]+)/$', views.client, name='client'),
    url(r'^client/new/$', views.client_new, name='client_new'),
    url(r'^client/(?P<pk>[0-9]+)/edit/$', views.client_edit, name='client_edit'),
    url(r'^client/(?P<pk>[0-9]+)/edit/client_delete$', views.client_delete, name='client_delete'),
    
    url(r'^groups', views.groups, name='groups'),
    url(r'^group/(?P<pk>[0-9]+)/$', views.group, name='group'),
    url(r'^group/new/$', views.group_new, name='group_new'),
    url(r'^group/(?P<pk>[0-9]+)/edit/$', views.group_edit, name='group_edit'),
    url(r'^group/(?P<pk>[0-9]+)/edit/group_delete$', views.group_delete, name='group_delete'),
]
