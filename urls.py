from django.urls import path
from .views import HomeView
from .views import ProjectCreateView
from .views import ProjectDetailView
from .views import ProjectEditView
from .views import ProjectDeleteView
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
import os

urlpatterns=[
    path("", HomeView.as_view(),name="all"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create/', ProjectCreateView.as_view(), name='project_create'),
    path('detail/<int:project_id>/', ProjectDetailView.as_view(), name='project_detail'),
    path('edit/<int:project_id>/', ProjectEditView.as_view(), name='project_edit'),
    path('delete/<int:project_id>/', ProjectDeleteView.as_view(), name='project_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
