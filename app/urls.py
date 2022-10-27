from . import views

from django.urls import path

urlpatterns = [
    path('whoareyou/', views.WhoAreYouView.as_view(), name= "whoareyouview")
]