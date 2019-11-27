from django.db import models

# Create your models here.

class Student(models.Model):
	id = models.IntegerField(primary_key = True)
	student_name = models.CharField(max_length = 50)
	student_faculty = models.CharField(max_length = 30)
	student_shift = models.CharField(max_length = 20)

	def __str__(self):
		return str(self.id)+", "+str(self.student_name)+", "+str(self.student_faculty)+", "+str(self.student_shift)