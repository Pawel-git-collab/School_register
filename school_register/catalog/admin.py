from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'kolokwium', 'aktywnosc', 'egzamin_koncowy', 'avgg', 'mark_EUR',
                    'mark_US', )

