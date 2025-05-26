from rest_framework import serializers
from .models import Category, Transaction
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ['user']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        Token.objects.create(user=user)
        return user

    def to_representation(self, instance):
        """Customize the response after creating the user."""
        token = Token.objects.get(user=instance)
        return {
            'username': instance.username,
            'email': instance.email,
            'token': token.key
        }
