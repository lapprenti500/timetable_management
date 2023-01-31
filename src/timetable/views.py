from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from timetable.forms import CreatePlanningForm
from timetable.models import Creneau


# Create your views here.
def homepage(request):
    creneaux = Creneau.objects.all()
    return render(request, 'timetable/index.html', context={'creneaux': creneaux})

def createPlanning(request):
    if request.method == 'POST':
        form = CreatePlanningForm(request.POST)
        if form.is_valid():
            create_planning = form.save(commit=False)
            create_planning.date_debut = form.cleaned_data['date_de_debut']
            create_planning.date_fin = form.cleaned_data['date_de_fin']
            create_planning.save()
        return HttpResponseRedirect(request.path)
            # créer une nouvelle « emplois » et la sauvegarder dans la db

            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection

    else:
        form = CreatePlanningForm()

    return render(request, 'timetable/createPlanning.html', {"form": form})
