from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST', 'PUT','PATCH', 'DELETE'])
def student_api(request, pk = None):
    if request.method == 'GET':
        # id = request.data.get('id')
        id = pk
        if id is not None:
            stu = Student.objects.get(pk = id)
            serializer = StudentSerializer(stu)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response({'msg': 'Successful Created'}, status=status.HTTP_201_CREATED)
    if request.method == 'PUT':
        # id = request.data.get('id')
        id = pk
        if id is not None:
            stu = Student.objects.get(pk = id)
            serializer = StudentSerializer(stu, data = request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response({'msg': 'Complete Data Successful Updated'}, status=status.HTTP_200_OK)
    if request.method == 'PATCH':
        # id = request.data.get('id')
        id = pk
        if id is not None:
            stu = Student.objects.get(pk = id)
            serializer = StudentSerializer(stu, data = request.data, partial = True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response({'msg': 'Partial Data Successful Updated'}, status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(pk = id)
        stu.delete()
        return Response({'msg': 'Successful Deleted'}, status=status.HTTP_200_OK)

    
