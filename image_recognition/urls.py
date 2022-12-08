from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('zobacz/<int:image_id>', views.detail, name='detail'),
    path('upload/', views.upload, name='upload'),
    path("delete/<int:image_id>", views.delete, name='delete'),
    path('list', views.list, name='list'),
    path('train', views.train, name='train'),
]