from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from myapp.serializers import FamilySerializers
from myapp.models import Family
from rest_framework.permissions import IsAuthenticated

class TESTView(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request, *args, **kwargs):
        qs = Family.objects.all().values()
        serializer = FamilySerializers(qs, many =  True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = FamilySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            Response(serializer.errors)
