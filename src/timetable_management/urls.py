
from django.contrib import admin
from django.urls import path, include

from timetable_management.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("timetable.urls")),
]
