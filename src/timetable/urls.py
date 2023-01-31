from django.urls import path

from .views import homepage, createPlanning

urlpatterns = [
    path('', homepage, name="timetable-homepage"),
    path('createPlanning', createPlanning, name='createPlanning')
]
