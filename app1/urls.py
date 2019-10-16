from django.urls import path
from . import views

urlpatterns = [
        path('text-analyzer/',views.TextSentimentView.as_view()),

]
