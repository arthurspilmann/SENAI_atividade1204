from django import forms
from .models import Colaborador, EPI, Emprestimo
import re

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome', 'cpf', 'setor']

        def clean_nome(self):
            
            nome = self.cleaned_data.get('nome', '').strip()  # Garantir que o nome não seja None e eliminar espaços extras
            if not nome:
                raise forms.ValidationError("O nome não pode estar vazio.")
            if re.search(r'\d', nome):  # Verificar se existe algum número no nome
                raise forms.ValidationError("O nome não pode conter números.")
            return nome
        

class EPIForm(forms.ModelForm):
    class Meta:
        model = EPI
        fields = ['nome', 'codigo', 'validade']

class EmprestimoForm(forms.ModelForm):
    nome_colaborador = forms.CharField(label='Nome do colaborador', required=False)

    class Meta:
        model = Emprestimo
        fields = ['colaborador', 'epi', 'data_emprestimo']

class RelatorioForm(forms.Form):
    data_inicio = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    data_fim = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

from django import forms

class FiltroEmprestimoForm(forms.Form):
    nome_colaborador = forms.CharField(label='Nome do colaborador', required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Digite o nome do colaborador'
    }))
