from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status

from .utils import send_code_to_user
from .models import OneTimePassword
from .serializers import UserRegisterSerializer, LoginUserSerializer


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



# class CreateUserView(generics.CreateAPIView):
#     serializer_class = UserSerializer   
    
# class RetrieveUpdateUserView(generics.RetrieveUpdateAPIView):
#     serializer_class = UserSerializer
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
    
#     def get_object(self):
#         return self.request.user
    

# class CreateTokenView(ObtainAuthToken):
#     serializer_class = AuthTokenSerializer

        

        