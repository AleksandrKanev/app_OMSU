from django import forms
from .models import *


class ApplicationForms(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'


class CardAnimalForms(forms.ModelForm):
    class Meta:
        model = CardAnimal
        fields = '__all__'


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'
