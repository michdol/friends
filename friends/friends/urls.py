from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('users/', include(('users.urls.urls', 'users'), namespace='users')),
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
]
