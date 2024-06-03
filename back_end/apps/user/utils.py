import random
from django.core.mail import EmailMessage
from .models import User, OneTimePassword
from django.conf import settings

def generateOtp():
    otp=""
    for i in range(6):
        otp += str(random.randint(1, 9))
    return otp 

def send_code_to_user(email):
    Subject = "Codigo de un solo uso para verificación de correo electrónico"
    otp_code = generateOtp()
    user = User.objects.get(email=email)
    current_site = 'SharyoMTTO'
    email_body = f"Hola {user.username}, gracias por registrarte en {current_site}, por favor verifique su correo electrónico con el siguiente codigo: {otp_code}."
    from_email = settings.DEFAULT_FROM_EMAIL
    
    OneTimePassword.objects.create(user=user, code=otp_code)
    
    send_email = EmailMessage(subject=Subject, body=email_body, from_email=from_email, to=[email])
    send_email.send(fail_silently=True)

def send_normal_email(data):
    email = EmailMessage(
        subject = data['email_subject'],
        body = data['email_body'],
        from_email = settings.EMAIL_HOST_USER,
        to = [data['to_email']]
    )
    email.send()