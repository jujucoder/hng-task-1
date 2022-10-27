from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework import status, response

# Create your views here.

class WhoAreYouView(GenericAPIView):


    def get(self, request, *args, **kwargs):
        slack_username="Jay Jay"
        backend = True
        age = 17
        bio = "Please Hire me"


        return response.Response({ "slackUsername": slack_username, "backend": backend, "age": age, "bio": bio }, status=status.HTTP_200_OK)


    


    
