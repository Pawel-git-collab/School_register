from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


class Student(models.Model):
    MARK_CHOICES = (
        ('mark_EUR', 'MARK_EUR'),
        ('mark_US', 'MARK_US'),
    )

    first_name = models.CharField(max_length=100, help_text='Podaj imię studenta')
    last_name = models.CharField(max_length=100, help_text='Podaj nazwisko studenta')
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')

    kolokwium = models.IntegerField(blank=False, verbose_name="kolokwium",
                                    validators=[MaxValueValidator(100), MinValueValidator(1)])
    aktywnosc = models.IntegerField(blank=False, verbose_name="aktywnosc",
                                    validators=[MaxValueValidator(100), MinValueValidator(1)])
    egzamin_koncowy = models.IntegerField(blank=False, verbose_name="egzamin koncowy",
                                          validators=[MaxValueValidator(100), MinValueValidator(1)])
    mark = models.CharField(max_length=8, choices=MARK_CHOICES, default='mark_EUR')

    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])

    def avgg(self):
        return round((self.kolokwium + self.aktywnosc + self.egzamin_koncowy) / 3, 2)

    def mark_EUR(self):
        if self.avgg() > 90:
            return 5
        elif self.avgg() > 70:
            return 4
        elif self.avgg() > 60:
            return 3
        else:
            return 'Niezaliczony'

    def mark_US(self):
        if self.avgg() > 90:
            return 'A'
        elif self.avgg() > 70:
            return 'B'
        elif self.avgg() > 60:
            return 'C'
        else:
            return 'Niezaliczony'
