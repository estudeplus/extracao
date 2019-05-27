from .models import Professor, Subject, Student

class ApiManager():

    def __init__(self):
        self._subject = None
        self._data = None
    
    def set_subject(self, subject):
        self._subject = subject
    
    def update(self):
        self._data = self._subject.get_state()