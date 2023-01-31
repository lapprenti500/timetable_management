from django.contrib import admin

# Register your models here.
from timetable.models import Dept, Filiere, Prof, Salle, Cours


@admin.register(Dept)
class DeptAdmin(admin.ModelAdmin):
    pass

@admin.register(Filiere)
class FiliereAdmin(admin.ModelAdmin):
    pass

@admin.register(Prof)
class ProfAdmin(admin.ModelAdmin):
    pass

@admin.register(Salle)
class SalleAdmin(admin.ModelAdmin):
    list_display = (
        "nom",
        "description",

    )

    list_editable = (
        "description",
    )

@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    pass