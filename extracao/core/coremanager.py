from .models import Document
from ..api.apimanager import ApiManager


class CoreManager():

    def __init__(self):
        self._api_manager = ApiManager()
        self._state = None
    
    def get_state(self):
        return self._state
    
    def _notify(self):
        self._api_manager.update()
    
    def load(self, state):
        self._state = state
        self._api_manager.set_subject(self)
        self._notify()