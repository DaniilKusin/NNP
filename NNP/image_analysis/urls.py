from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.get_analysis_page, name='home'),
    path('upload-image/', views.upload_image, name='upload_image'),
    path('analyze/', views.analyze, name='analyze'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)