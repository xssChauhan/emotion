from rest_framework import serializers

from .models import Emotion

import json


class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = "__all__"
