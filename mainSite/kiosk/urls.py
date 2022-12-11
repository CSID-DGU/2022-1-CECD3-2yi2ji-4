from django.urls import path

from . import views

app_name = "kiosk" # 앱 이름 설정
urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.upload, name='upload'),
    path('testIndex', views.objectIndex, name='objectIndex'),
    path('kakaoApi/', views.kakaoApi, name="kakaoApi"),
    path('sttFileApi/', views.sttFileApi, name="sttFileApi"),
    path('sttMicApi/', views.sttMicApi, name="sttMicApi"),
    path('ttsApi/', views.ttsApi, name="ttsApi"),
    path('roi/', views.roi, name="roi"),
    path('roiResult/', views.roiResult, name="roiResult"),
]