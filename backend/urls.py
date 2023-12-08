from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

urlpatterns = [
	path("admin/", admin.site.urls),
	path("api-auth/", include("rest_framework.urls")),
	path("", include("room.urls")),
	path("", include("util.urls")),
	path("", include("review.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [re_path(r"^(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT})]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)