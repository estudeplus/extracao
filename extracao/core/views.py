from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import DocumentForm
from .models import Document
from .coremanager import CoreManager
from .states import Extensions

class FormView(LoginRequiredMixin, FormView):

    template_name = 'uploadfile.html'
    form_class = DocumentForm

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, 'File uploaded')
        return reverse_lazy('upload-file')
    
    def get_file_type(self, file):
        if(file.path.endswith('.xlsx')):
            return 'xlsx'
        return 'csv'

    def form_valid(self, form):
        '''
        Receive form already validated
        '''
        document = form.save()
        document.extension = self.get_file_type(document.document)
        document.save()
        core = CoreManager()
        core.load(document)
        return super().form_valid(form)

