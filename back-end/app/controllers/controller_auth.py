import random
import string
from tarfile import TarFile

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, \
    ListCreateAPIView
from app.models import User
from rest_framework.decorators import api_view
from django.core.mail import send_mail, EmailMessage
from settings.base import EMAIL_HOST_USER
from app.serializers import UserSerializer
from rest_framework.authtoken.models import Token


class FetchUserView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response(UserSerializer(self.request.user).data)


class FetchUsersView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()


class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
        })


@api_view(['POST'])
def token_is_valid(request):
    token = request.data.get('token', '')
    return Response(status=200, data={'valid': len(Token.objects.filter(key=token)) > 0})
