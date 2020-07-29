from rest_framework import serializers
from app.models import *


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name', 'flag', 'zip_code']
        model = Country


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image


class UserSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    avatar = ImageSerializer(read_only=True, required=False)

    class Meta:
        fields = "__all__"
        model = User
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},
            'full_name': {'read_only': True}
        }

    def save(self, **kwargs):
        user = User.objects.create_user(**{**self.data.serializer.initial_data})
        user.set_password(self.data.serializer.initial_data['password'])
        return user
