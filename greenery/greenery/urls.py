from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogs.urls')),
    path('contributors/', include('django.contrib.auth.urls')),
    path('contributors/', include('contributors.urls'))
]

urlpatterns += staticfiles_urlpatterns()