from django.urls import re_path
 
from forms import views

app_name = 'forms'

urlpatterns = [
 
    # /forms/
    re_path(r'^$', views.IndexView.as_view(), name='home'),
 
    # forms/document/entry
    re_path(r'^document/entry/$',views.DocumentEntry.as_view(),name='document-entry'),
 
    # forms/document/2
    re_path(r'^document/(?P<pk>[0-9]+)/$', views.DocumentUpdate.as_view(), name='document-update'),
 
    # forms/document/(?P<pk>[0-9]+)/delete
    re_path(r'document/(?P<pk>[0-9]+)/delete$', views.DocumentDelete.as_view(), name='document-delete'),
 
]