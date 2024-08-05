"""
URL configuration for clinic_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from main import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('admin-page/', views.admin_page, name='admin_page'),
    path('dokter-page/', views.dokter_page, name='dokter_page'),
    path('pasien-page/', views.pasien_page, name='pasien_page'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('dokter-page/', views.dokter_page, name='dokter_page'),
    path('dokter-dashboard/', views.dokter_dashboard, name='dokter_dashboard'),
    path('pasien-page/', views.dokter_page, name='pasien_page'),
    path('pasien-dashboard/', views.dokter_dashboard, name='pasien_dashboard'),
    path('logout/', views.logout_view, name='logout'),

]
