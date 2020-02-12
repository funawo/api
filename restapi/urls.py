from rest_framework import routers
from django.conf.urls import url
from .views import SampleAPI, CouponAPI

urlpatterns = [
  url('test', SampleAPI.as_view()),
  url('coupon', CouponAPI.as_view())
]
