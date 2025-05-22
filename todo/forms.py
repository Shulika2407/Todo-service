from django import forms
from todo.models import Task, Tag
from django.contrib.auth import get_user_model


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Tag.objects.all(),
    )

    class Meta:
        model = Task
        fields = "__all__"