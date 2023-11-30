from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'settingspage'
urlpatterns = [
    path('', views.settingsPage, name='settingsPage'),
    path('general/', views.generalPage, name='gerenalPage'),
    path('posts/', views.postPage, name='postPage'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_URL)