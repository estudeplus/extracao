from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView

from .forms import DocumentForm

class FormView(LoginRequiredMixin, FormView):

    template_name = 'uploadfile.html'
    form_class = DocumentForm

    def form_valid(self, form):
        '''
        Receive form already validated
        '''
        pass
