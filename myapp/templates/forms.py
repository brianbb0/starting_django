from django import forms

class Create_task(forms.Form):
    title = forms.CharField(label="Título de tarea", max_length=200)
    description = forms.CharField(widget=forms.Textarea, label="Descripción de la tarea", max_length=200)

class Create_project(forms.Form):
    name = forms.CharField(label="Título de tarea", max_length=200)