from rest_framework import serializers

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
#		fields  = ('id',student_name','student_faculty','student_shift')
		fields = '__all__'