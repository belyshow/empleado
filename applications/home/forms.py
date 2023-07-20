from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):
    class Meta:
         model = Prueba
         fields = (
            'titulo',
            'subtitulo',
            'cantidad',
        )
         
         widgets = {
             'titulo':forms.TextInput(
                 attrs={
                     'placeholder':'Ingresa un titulo aqui'
                 }
             ),
              'subtitulo':forms.TextInput(
                 attrs={
                     'placeholder':'Ingresa un subtitulo aqui'
                 }
             ),
              'cantidad':forms.TextInput(
                 attrs={
                     'placeholder':'Cantidad superior a 10'
                 }
             )
         }

    def clean_cantidad(self):
        cantidad=self.cleaned_data['cantidad']
        if cantidad <10:
            raise forms.ValidationError('Ingrese un valor superior a 10')
        return cantidad
