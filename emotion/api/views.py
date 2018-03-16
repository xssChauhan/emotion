from django.shortcuts import render

from .models import Emotion
from .serializers import EmotionSerializer
from .authentication import Custom

from rest_framework import generics
# Create your views here.



class EmotionView(generics.CreateAPIView):
    serializer_class = EmotionSerializer
    queryset = Emotion.objects
    authentication_classes = [Custom] 




