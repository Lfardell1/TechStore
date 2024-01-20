from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
urlpatterns = [
    # use custom login backend
    path('admin/', admin.site.urls),
    path('', include('Store.urls')),
]
