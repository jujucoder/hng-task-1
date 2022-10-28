from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework import status, response

# Create your views here.

class WhoAreYouView(GenericAPIView):


    def get(self, request, *args, **kwargs):
        slack_username="JayJayDev"
        backend = True
        age = 17
        bio = "I'm a Computer science undergraduate, I Kill Pythons and fight bugs"


        return response.Response({ "slackUsername": slack_username, "backend": backend, "age": age, "bio": bio }, status=status.HTTP_200_OK)


    


    
