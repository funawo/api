from rest_framework import routers
from django.conf.urls import url
from .views import SampleAPI

urlpatterns = [
  url('test', SampleAPI.as_view())
]
