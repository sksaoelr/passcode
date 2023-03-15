from django.contrib import admin
from django.urls import path, include
from passcode.views import base_views, category_veiws, notice_views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('passcode/', include('passcode.urls')),
    path('common/', include('common.urls')),
    # path('', base_views.index, name='index'),  # '/' 에 해당되는 path
    path('', base_views.main, name='main'),  # '/' 에 해당되는 path
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'common.views.page_not_found'