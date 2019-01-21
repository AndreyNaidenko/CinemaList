from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('films/', include('app_cinema_list.urls')),
    path('admin/', admin.site.urls),
]
