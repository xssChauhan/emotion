from rest_framework import authentication
from rest_framework import exceptions

from django.conf import settings

class Custom(authentication.BaseAuthentication):
    
    def authenticate(self,request):
        email = request.data.get('email')
        print(request.data)
        if not email or email not in settings.AUTH_EMAILS:
            raise exceptions.AuthenticationFailed("You're drunk, go home")
        else:
            return None



