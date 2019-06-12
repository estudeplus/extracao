import pandas as pd

from .models import Professor, Subject, Student
from ..core.states import Extensions

class ApiManager():

    def __init__(self):
        self._core_manager = None
        self._data = None
    
    def set_subject(self, core):
        self._core_manager = core
    
    def update(self):
        self._data = self._core_manager.get_state()
        if(self._data.extension == 'xlsx'):
            print("File Extension: xlsx")
            self.load_xlsx(self._data.document)
        else:
            print("File Extension: csv")
    
    def load_xlsx(self, document_path):
        df = pd.read_excel(document_path)
        if(self.check_data(df.columns)):
            print("Document is correct")
            return True
        else:
            print("Document is incorrect")
            return False

    def load_csv(self, document_path):
        pass
    
    def check_data(self, columns):

        indexes = ['código', 'disciplina', 'turma',
                    'professor', 'email do professor',
                    'aluno', 'matrícula', 'email do aluno', 
                    'menção', 'ira', 'nota final']

        ## All string to lowecase
        columns = [x.lower() for x in list(columns)]
        if(set(indexes).issuperset(set(columns))):
            return True
        return False
