from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('image_analysis.urls')),
    path('user_profile/', include('user_profile.urls')),
    path('image-history/', include('image_history.urls')),
    path('about/', include('about.urls')),
]