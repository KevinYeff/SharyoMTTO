from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import smart_str, DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from .utils import send_code_to_user
from .models import OneTimePassword, User
from .serializers import (UserRegisterSerializer, 
                          LoginUserSerializer, 
                          PasswordResetRequestViewSerializer, 
                          SetNewPasswordSerializer,
                          LogoutUserSerializer,
                          ProfileUserSerializer)


# Create your views here.

class RegisterUserView(GenericAPIView):
    serializer_class = UserRegisterSerializer
    
    def post(self, request):
        user_data = request.data
        serializer=self.serializer_class(data=user_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user=serializer.data
            send_code_to_user(user['email'])
            # Envio de correo user['email']
            return Response({
                'data': user,
                'message': f'Gracias por registrarte, un codigo de verifiación fue enviado a su correo electrónico.'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_401_BAD_REQUEST)
            
class VerifyUserEmail(GenericAPIView):
    def post(self, request):
        otpcode = request.data.get('otp')
        try:
            user_code_obj = OneTimePassword.objects.get(code=otpcode)
            user = user_code_obj.user
            if not user.is_verified:
                user.is_verified = True
                user.save()
                return Response({
                    'message': 'Correo electronico verificado con exito.'
                }, status=status.HTTP_200_OK)
            return Response({
                'message': 'Codigo invalido, correo electronico ya verificado'
            }, status=status.HTTP_204_NO_CONTENT)
        
        except OneTimePassword.DoesNotExist:
            return Response({
                'message': 'No se indicó el codigo de verificación'
            }, status=status.HTTP_404_NOT_FOUND)

class LoginUserView(GenericAPIView):
    serializer_class = LoginUserSerializer
    def post(self, request):
        serializer=self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class TestAuthenticationView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        data={
            'msg': 'funciona'
        }
        return Response(data, status=status.HTTP_200_OK)

class PasswordResetRequestView(GenericAPIView):
    serializer_class = PasswordResetRequestViewSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        return Response({'message': "Un link ha sido enviado a su correo electrónico para reiniciar su contraseña."}, status=status.HTTP_200_OK)


class PasswordResetConfirm(GenericAPIView):
    def get(self, request, uidb64, token):
        try:
            user_id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=user_id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'message': 'El token es invalido o ha expirado.'}, status=status.HTTP_401_UNAUTHORIZED)
            return Response({'success': True, 'message': 'Credenciales validas.', 'uidb64': uidb64, 'token': token}, status=status.HTTP_200_OK)
        
        except DjangoUnicodeDecodeError:
            return Response({'message': 'El token es invalido o ha expirado.'}, status=status.HTTP_401_UNAUTHORIZED)

class SetNewPassword(GenericAPIView):
    serializer_class = SetNewPasswordSerializer
    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'message': 'Contraseña actualizada exitosamente.'}, status=status.HTTP_200_OK)
        
class LogoutUserView(GenericAPIView):
    serializer_class = LogoutUserSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Sesión cerrada exitosamente.'}, status=status.HTTP_200_OK)
        
class ProfileUserView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProfileUserSerializer
    
    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(user=user)
    
    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request):
        serializer = self.serializer_class(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request):
        user = request.user
        user.delete()
        return Response({'message': 'Usuario eliminado exitosamente.'}, status=status.HTTP_200_OK)
