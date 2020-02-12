from rest_framework import serializers
from .models import User, Coupon


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
          'id',
          'name'
        )


class CouponSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coupon
        fields = (
            'code',
            'benefit',
            'explanation',
            'image',
            'store',
            'start',
            'deadline',
            'status'
        )
