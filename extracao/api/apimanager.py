from ..core.models import Document
from .models import Professor, Subject, Student

class ApiManager():

    def __init__(self):
        self._subject = None
        self._state = None
    
    def update(self):
        pass