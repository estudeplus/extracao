import pandas as pd

from django.shortcuts import redirect

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
        self.load()

    def load(self):
        df = self.get_data()
        if(self.check_data(df.columns)):
            # If correct, it's time to add the data to the models
            for index, row in df.iterrows():
                print(row['código'], row['disciplina'])
                subject = self.check_subject(row)
                if(subject):
                    pass
                else:
                    # Maybe adding all data models in the lines
                    # above give the chance to pop the already used
                    # data so the code does not pass through the same data
                    continue
        else:
            # If not correct, notify the view that the uploaded document is not correct
            pass
    
    def get_subject_students(self, data):
        pass
    
    def get_professor(self, row):

        # Get a existent professor, or create one

        try:
            professor = Professor.objects.get(name=row['professor'])
        except Professor.DoesNotExist:
            professor = Professor(
                name=row['professor'],
                email=row['email'],
            )
            professor.save()
        
        return professor
    
    def check_subject(self, row):

        # Get a existent subject, or create one

        try:
            subject = Subject.objects.get(
                code=row['código'],
                class_code=row['turma']
            )
            return False
        except Subject.DoesNotExist:
            subject = Subject(
                code=row['código'],
                name=row['disciplina'],
                class_code=row['turma']
            )
            subject.save()
            professor = self.get_professor(row)
            subject.professor = professor
            subject.save()

            return subject

    def get_data(self):

        if(self._data.extension == 'xlsx'):
            df = pd.read_excel(self._data.document)
        else:
            df = pd.read_csv(self._data.document, delimiter = ',')
        
        df.columns = [x.lower() for x in df.columns]
        return df

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
