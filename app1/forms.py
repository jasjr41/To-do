from django import forms

from app1.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            "task": forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'datepicker'

        })}