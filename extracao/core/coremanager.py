from .models import Document
from ..api.apimanager import ApiManager


class CoreManager():

    def __init__(self, state):
        self._observer = None
        self._state = state
    
    def attach(self, observer):
        observer._subject = self
        self._observer = observer
    
    def get_state(self):
        return self._state.document
    
    def _notify(self):
        pass
    
    def load(self):
        pass