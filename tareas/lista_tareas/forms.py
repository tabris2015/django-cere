from django import forms
from .models import Cliente

class CrearTareaForm(forms.Form):
    texto = forms.CharField(label='Texto ', max_length=300)
    prioridad = forms.IntegerField(label='Prioridad ', max_value=10, min_value=0)


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'edad', 'fecha_nacimiento', 'score']