from django import forms
from django.conf import settings
from django.forms import ModelForm
# import pdb
#from django.utils.translation import ugettext_lazy as _
import logging
from .models import *


class NewProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewProjectForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Portfolio
        fields = '__all__'

