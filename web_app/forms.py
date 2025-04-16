from django import forms
from .models import todolist


class TodoListForm(forms.ModelForm):
    class Meta:
        model = todolist
        fields = ['name', 'due_date', 'description', 'status', 'people_involved']