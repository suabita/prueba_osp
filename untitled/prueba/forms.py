from django.forms import ModelForm, TextInput, Select

from prueba.models import Prueba


class PruebaDBForm(ModelForm):

    class Meta:
        model = Prueba
        fields = '__all__'
        widgets = {'pregunta_uno': TextInput(attrs={'class':'form-control'}),
                   'respuesta_uno_a': TextInput(attrs={'class': 'form-control'}),
                   'respuesta_uno_b': TextInput(attrs={'class': 'form-control'}),
                   'respuesta_uno_c': TextInput(attrs={'class': 'form-control'}),
                   'respuesta_uno_d': TextInput(attrs={'class': 'form-control'}),
                   'respuesta_correcta_uno': Select(attrs={'class': 'form-control'}),
                   'pregunta_dos': TextInput(attrs={'class': 'form-control'}),
                   'respuesta_dos_a': TextInput(attrs={'class': 'form-control'}),
                   'respuesta_dos_b': TextInput(attrs={'class': 'form-control'}),
                   'respuesta_dos_c': TextInput(attrs={'class': 'form-control'}),
                   'respuesta_dos_d': TextInput(attrs={'class': 'form-control'}),
                   'respuesta_correcta_dos': Select(attrs={'class': 'form-control'}),
                   'pregunta_tres': TextInput(attrs={'class': 'form-control'}),
                   'respuesta_tres_a': TextInput(attrs={'class': 'form-control'}),
                   'respuesta_tres_b': TextInput(attrs={'class': 'form-control'}),
                   'respuesta_tres_c': TextInput(attrs={'class': 'form-control'}),
                   'respuesta_tres_d': TextInput(attrs={'class': 'form-control'}),
                   'respuesta_correcta_tres': Select(attrs={'class': 'form-control'}),
                   'pregunta_cuatro': TextInput(attrs={'class': 'form-control'}),
                   'respuesta_cuatro_a': TextInput(attrs={'class': 'form-control'}),
                   'respuesta_cuatro_b': TextInput(attrs={'class': 'form-control'}),
                   'respuesta_cuatro_c': TextInput(attrs={'class': 'form-control'}),
                   'respuesta_cuatro_d': TextInput(attrs={'class': 'form-control'}),
                   'respuesta_correcta_cuatro': Select(attrs={'class': 'form-control'}),
                   'pregunta_cinco': TextInput(attrs={'class': 'form-control'}),
                   'respuesta_cinco_a': TextInput(attrs={'class': 'form-control'}),
                   'respuesta_cinco_b': TextInput(attrs={'class': 'form-control'}),
                   'respuesta_cinco_c': TextInput(attrs={'class': 'form-control'}),
                   'respuesta_cinco_d': TextInput(attrs={'class': 'form-control'}),
                   'respuesta_correcta_cinco': Select(attrs={'class': 'form-control'}),

                   }