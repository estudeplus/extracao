from rest_framework import serializers

from .models import Subject, Professor, Student


class StudentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Student
		fields = ('id','name', 'email', 'ira', 'grade', 'mention','student_code')


class ProfessorSerializer(serializers.ModelSerializer):

	class Meta:
		model = Professor
		fields = ('id','name', 'email')


class SubjectSerializer(serializers.ModelSerializer):
    professor = ProfessorSerializer()
    tutors = StudentSerializer(many=True)
    class Meta:
        model = Subject
        fields = ('id','code','name', 'classcode', 'professor','tutors',)