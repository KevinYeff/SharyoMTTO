from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    password2 = serializers.CharField(max_length=68, min_length=6, write_only=True)
    
    class Meta:
        model = User
        fields = ['email', 'username', 'name', 'last_name', 'mobile', 'password', 'password2']
        
    def validate(self, attrs):
        password = attrs.get('password', '')
        password2 = attrs.get('password2', '')
        if password != password2:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        return attrs
        
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            username = validated_data.get('username'),
            name = validated_data.get('name'),
            last_name = validated_data.get('last_name'),
            mobile = validated_data.get('mobile'),
            password = validated_data.get('password'),
        )
        
        return user
    
class LoginUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=30, min_length=6)
    password = serializers.CharField(max_length=68, write_only=True)
    full_name = serializers.CharField(max_length=255, read_only=True)
    access_token = serializers.CharField(max_length=255, read_only=True)
    refresh_token = serializers.CharField(max_length=255, read_only=True)
    
    class Meta:
        model = User
        fields = ['email', 'password', 'full_name', 'access_token','refresh_token']
        
        
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        request = self.context.get('request')
        user = authenticate(
            request,
            email=email,
            password=password
        )
        if not user:
            raise AuthenticationFailed("Credenciales invalidas, intente de nuevo")
        user_tokens = user.tokens()
        
        return {
            'email': user.email,
            'full_name': user.get_full_name,
            'access_token': str(user_tokens.get('access')),
            'refresh_token': str(user_tokens.get('refresh')),
        }
    
    
    
#     def update(self, instance, validated_data):
#         password = validated_data.pop('password', None)
#         user = super().update(instance, validated_data)
        
#         if password:
#             user.set_password(password)
#             user.save()
        
#         return user

# class AuthTokenSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(style={'input_type': 'password'})
    
#     def validate(self, data):
#         email = data.get('email')
#         password = data.get('password')
#         user = authenticate(
#             request=self.context.get('request'),
#             username=email,
#             password=password
#         )
        
#         if not user:
#             raise serializers.ValidationError('No se pudo autenticar', code='authorization')
        
#         data['user'] = user
#         return data