
from wtforms_alchemy import ModelForm

from app.models import Patient, PatientService


class PatientForm(ModelForm):
    class Meta:
        model = Patient



class PatientServiceForm(ModelForm):
    class Meta:
        model = PatientService


