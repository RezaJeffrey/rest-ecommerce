from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/api/v1/', include('users.api.v1.urls', namespace='users:api:v1')),
    path('categories/api/v1/', include('category.api.v1.urls', namespace='categories:api:v1')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

