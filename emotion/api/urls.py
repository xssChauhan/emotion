from django.urls import path

from .views import EmotionView



urlpatterns = [
    path('emotion/', EmotionView.as_view()),
]
