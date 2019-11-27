from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

# Create your views here.


class studentList(APIView):
	'''Lists all the students in the database and adds the content to the database'''

	def get(self, request):
		student = Student.objects.all()

		serializer = StudentSerializer(student, many = True)

		return Response(serializer.data)


	def post(self, request):
		serializer = StudentSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class studentDetail(APIView):
	'''Detail of each individual students will be displayed while their ID number (pk)is given in a url pattern'''

	def get_object(self,pk):
		try:
			return Student.objects.get(pk = pk)
		except Student.DoesNotExist:
			return Http404

	def get(self, request, pk):
		student = self.get_object(pk)
		serializer = StudentSerializer(student)
		return Response(serializer.data)

	def put(sefl, request,pk):
		student = self.get_object(pk)
		serializer = StudentSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	def delete(self, request,pk):
		student = self.get_object(pk)
		student.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
