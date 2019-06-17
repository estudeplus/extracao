from rest_framework import viewsets

from rest_framework.views import APIView

from .models import Subject
from .serializers import SubjectSerializer
from .utils.responses import ResponseUtils as responseutils
from .utils.subject import SubjectUtils as subjectutils


from rest_framework import viewsets

class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer