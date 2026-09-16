from django import forms

from .models import Veiculo


class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = [
            'placa', 'marca', 'modelo', 'ano', 'cor', 'cliente', 'ativo',
        ]

    def clean_placa(self):
        return self.cleaned_data['placa'].strip().upper()
