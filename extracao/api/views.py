from rest_framework import viewsets

from rest_framework.views import APIView

from .models import Subject
from .serializers import SubjectSerializer
from .utils.responses import ResponseUtils as responseutils
from .utils.subject import SubjectUtils as subjectutils


class GeneralEnpoint(APIView):

  def get(self, request, subject_id=None):
    if(subject_id):
      subject = subjectutils.get_by_id(subject_id)
      if(subject):
        serializer = SubjectSerializer(subject)
        return responseutils.success_data(serializer.data)
      else:
        return responseutils.not_found("Subject Not Found")
    else:
      subjects = subjectutils.get_all()
      for sub in subjects:
        print(sub.name)
        print(sub.code)
      if(len(subjects)>0):
        serializer = SubjectSerializer(subjects, many=True)
        return responseutils.success_data(serializer.data)
      else:
        return responseutils.not_found("0 subjects Found")
