from django import forms
from .models import Student


class Mark(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
