from rest_framework.views import APIView
from rest_framework.response import Response
# from .models import User
# from .serializers import UserSerializer


class SampleAPI(APIView):

    def get(self, request):
        # result = User.objects.all()
        # user = UserSerializer(result, many=True)
        # return Response(user.data)
        return Response({ 'fuanwo': 'funashi'})
