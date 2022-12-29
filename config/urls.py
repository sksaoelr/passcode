from django.contrib import admin
from django.urls import path, include
from passcode.views import base_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('passcode/', include('passcode.urls')),
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
]


handler404 = 'common.views.page_not_found'