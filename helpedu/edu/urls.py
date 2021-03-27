from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.index,name='Home'),
    path('schools/',views.schools,name='schools'),
    path('donate/',views.donate,name='donate'),
    path('content/',views.content,name='content'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
