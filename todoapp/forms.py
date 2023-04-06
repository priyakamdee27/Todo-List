from django import forms
from .models import TodoApp


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoApp
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.fields['details'].required = False
