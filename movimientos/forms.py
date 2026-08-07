from django import forms
from .models import Entrada, Salida


class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['fecha', 'no_comprobante', 'producto', 'cantidad']  # <- sin precio_compra
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'no_comprobante': forms.TextInput(attrs={'class': 'form-control'}),
            'producto': forms.Select(attrs={'class': 'form-select'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }
class SalidaForm(forms.ModelForm):
    class Meta:
        model = Salida
        fields = ['fecha', 'no_comprobante', 'producto', 'cantidad', 'villa']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'no_comprobante': forms.TextInput(attrs={'class': 'form-control'}),
            'producto': forms.Select(attrs={'class': 'form-select'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'villa': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        producto = cleaned_data.get('producto')
        cantidad = cleaned_data.get('cantidad')

        if producto and cantidad:
            if cantidad > producto.existencia:
                raise forms.ValidationError(
                    f'No hay suficiente stock. Existencia disponible: {producto.existencia}'
                )
        return cleaned_data