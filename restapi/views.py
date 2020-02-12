from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Coupon
from .serializers import UserSerializer, CouponSerializer


class SampleAPI(APIView):

    def get(self, request):
        result = User.objects.all()
        user = UserSerializer(result, many=True)
        return Response(user.data)


class CouponAPI(APIView):

    def get(self, request):
        result = Coupon.objects.all()
        coupon = CouponSerializer(result, many=True)
        return Response(coupon.data)
