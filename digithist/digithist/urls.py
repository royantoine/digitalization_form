"""digithist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from documents import views
from digithist import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('document/add_folder', views.folder_create, name = 'folder-create'),
    path('', views.document_list, name='document-list'),
    path('document/', views.document_list, name='document-list'),
    path('document/<int:id>/', views.document_detail, name='document-detail'),
    path('document/add/', views.document_create, name='document-create'),
    path('document/<int:id>/update', views.document_update, name='document-update'),
    path('document/<int:id>/delete', views.document_delete, name='document-delete')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
