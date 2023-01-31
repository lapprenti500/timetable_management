from django import forms
from timetable.models import Creneau


class CreatePlanningForm(forms.ModelForm):
    class Meta:
        model = Creneau
        exclude = ['date_debut', 'date_fin']

        labels = {
            'filiere': 'Filière',
            'prof': 'Professeur'
        }
    date_de_debut = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    date_de_fin = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
