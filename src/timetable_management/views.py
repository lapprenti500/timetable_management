from django.shortcuts import render


def index(request):
    return render(request, 'timetableManagement/index.html')
