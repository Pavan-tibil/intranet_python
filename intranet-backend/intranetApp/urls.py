# imported modules

from django.contrib import admin
from rest_framework import routers
from django.urls import path,include
from .views import *
router = routers.DefaultRouter()
from django.conf.urls.static import static
from django.conf import settings

# end points to run the API's

urlpatterns = [
    path('getLatestNews',Latestnews.as_view()),
    path('imageFields/',image_files.as_view()),
    path('comments',comments.as_view()),
    path('comments/<int:pk>', comments_by_id.as_view()),
    path('media',ImageViewSet.as_view()),
    path('staffDirectory',staff_directory.as_view()),
    path('staffDirectory/<int:pk>',staff_directory.as_view()),
    path('getuserlist',get_user_list.as_view()),
    path('referCandidate',referCandidates.as_view()),
    path('awardyears',awardyear.as_view()),
    path('awards/<str:year>',awards.as_view()),
    path('vacancy',vacancy.as_view()),
    path('forum',forum.as_view()),
    path('login/',LoginAPIView.as_view()),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)