from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Assistant
from .serializers import AssistantSerializer

@api_view(['POST'])
def create_assistant(request):
    serializer = AssistantSerializer(data=request.data)
    if serializer.is_valid():
        assistant = serializer.save()
        return Response({'id': assistant.id})
    return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def assistant_detail(request, assistant_id):
    assistant = get_object_or_404(Assistant, pk=assistant_id)
    if request.method == 'GET':
        serializer = AssistantSerializer(assistant)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AssistantSerializer(assistant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        assistant.delete()
        return Response(status=204)

