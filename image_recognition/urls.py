from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('zobacz/<int:image_id>', views.detail, name='detail'),
    path('upload/', views.upload, name='upload'),
]