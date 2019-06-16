from django.urls import include, path
from rest_framework import routers
from .views import GeneralEnpoint

urlpatterns = [
    path(
        'subjects/',
        GeneralEnpoint.as_view(),
        name="subject-general-endpoint"
    ),
]