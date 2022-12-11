from django.urls import path

from . import views

app_name = "object" # 앱 이름 설정
urlpatterns = [
  path('', views.barcode, name='barcode'),
  path('send/', views.send, name="send"),
]