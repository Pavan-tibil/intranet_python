# Project URLS

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.views.static import serve

# URL paths to connect Application from project

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include("intranetApp.urls")),  # path for APP urls
    path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}), # path for media file

]
