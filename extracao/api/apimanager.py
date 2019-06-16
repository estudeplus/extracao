import pandas as pd

from django.shortcuts import redirect

from .models import Professor, Subject, Student


class ApiManager():

    def __init__(self):
        self._core_manager = None
        self._data = None

    def set_subject(self, core):
        self._core_manager = core

    def update(self):
        Subject.objects.all().delete()
        Professor.objects.all().delete()
        Student.objects.all().delete()
        self._data = self._core_manager.get_state()
        self.load()

    def load(self):
        df = self.get_data()
        df = df.fillna(0)
        if(self.check_data(df.columns)):
            # If correct, it's time to add the data to the models
            for index, row in df.iterrows():
                subject = self.check_subject(row)
                self.save_professor(row, subject)
                self.save_student(row, subject)
        else:
            # If not correct, notify the view that the uploaded document is not correct
            pass
    
    def save_student(self, row, subject):

        try:
            student = Student.objects.get(name=row['aluno'])
            student.subject = subject
            student.save()
        except Student.DoesNotExist:
            print(1)
            print(row)
            student = Student(
                name=row['aluno'],
                email=row['email do aluno'],
                student_code=row['matrícula'],
                ira=row['ira'],
                grade=row['nota final'],
                mention=row['menção'],
                subject=subject
            )
            student.save()
    
    def save_professor(self, row, subject):

        # Get a existent professor, or create one

        try:
            professor = Professor.objects.get(name=row['professor'])
        except Professor.DoesNotExist:
            professor = Professor(
                name=row['professor'],
                email=row['email do professor'],
            )
            professor.save()
        
        subject.professor = professor
        subject.save()
    
    def check_subject(self, row):

        # Get a existent subject, or create one

        try:
            subject = Subject.objects.get(
                code=row['código'],
            )
        except Subject.DoesNotExist:
            subject = Subject(
                code=row['código'],
                name=row['disciplina'],
            )
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
