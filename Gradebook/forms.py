from django import forms
from Gradebook.models import Semester, Course

class CreateSemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = {'year', 'semester'}
        widgets = {
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'semester': forms.TextInput(attrs={'class': 'form-control'}),

        }

class UpdateSemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = {'year', 'semester'}