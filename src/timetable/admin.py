from django.contrib import admin

# Register your models here.
from timetable.models import Dept, Filiere, Prof, Salle, Cours


@admin.register(Dept)
class DeptAdmin(admin.ModelAdmin):
    pass

@admin.register(Filiere)
class DeptAdmin(admin.ModelAdmin):
    pass

@admin.register(Prof)
class DeptAdmin(admin.ModelAdmin):
    pass

@admin.register(Salle)
class DeptAdmin(admin.ModelAdmin):
    list_display = (
        "nom",
        "description",
    )

@admin.register(Cours)
class DeptAdmin(admin.ModelAdmin):
    pass