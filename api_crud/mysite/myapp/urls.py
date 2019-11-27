from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	path('student',views.studentList.as_view()),
	path('student/<int:pk>',views.studentDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)