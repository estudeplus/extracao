from .models import Professor, Subject, Student

class ApiManager():

    def __init__(self):
        self._core_manager = None
        self._data = None
    
    def set_subject(self, core):
        self._core_manager = core
    
    def update(self):
        self._data = self._core_manager.get_state()
        print(self._data)
