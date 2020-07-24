
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from . import views

# admin.site.site_header = "ADMINISTRATOR PAGE"
admin.site.site_title = " "
admin.site.index_title = "TIMEKEEPING"


urlpatterns = [
    # path('', admin.site.urls),
    path('admin/', admin.site.urls),
    path('cfmc/', include('cfmc.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)