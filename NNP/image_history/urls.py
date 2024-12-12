from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_history, name='image_history'),
    path('delete/<int:image_id>/', views.delete_image, name='delete_image'),
]
