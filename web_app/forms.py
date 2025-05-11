from django import forms
from .models import todolist
from django.contrib.auth.models import User

class TodoListForm(forms.ModelForm):
    assigned_to = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-select'}),
        required=False
    )

    class Meta:
        model = todolist
        fields = ['name', 'due_date', 'description', 'status', 'assigned_to']
