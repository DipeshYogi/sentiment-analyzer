from django.shortcuts import render
from .serializers import TextSerializer
from rest_framework.views import APIView
from .analysis import analyseText
from rest_framework.response import Response
from rest_framework import status

class TextSentimentView(APIView):
    serializer_class = TextSerializer

    def post(self,request,format=None):
        serializer = self.serializer_class(data=request.data)
        score = ''
        if serializer.is_valid():
            text = serializer.validated_data.get('text')

            score = analyseText(text)
        else:
             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        return Response({'message':score})
