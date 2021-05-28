from django.shortcuts import render
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import Oauth2Client
from dj_rest_auth.registration.views import SocialLoginView



# Create your views here.


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    # callback_url = 
    client_class = Oauth2Client