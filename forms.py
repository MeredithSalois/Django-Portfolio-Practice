from django.forms import ModelForm
from portfolio.models import Project

class ProjectForm (ModelForm):
    class Meta:
        model=Project
        fields="__all__"