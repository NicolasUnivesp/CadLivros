from django import forms
from .models import Livro, Emprestimo

class LivroForm(forms.ModelForm):
    data_cadastro = forms.DateField(
        widget=forms.TextInput(
            attrs={"type":"date"}
        )
    )
    class Meta:
        model = Livro
        fields = ['titulo_completo', 'data_cadastro', 'emprestado']

class EmprestimoForm(forms.ModelForm):
    data_retirada = forms.DateField(
        widget=forms.TextInput(
            attrs={"type":"date"}
        )
    )
    data_devolucao = forms.DateField(
        widget=forms.TextInput(
            attrs={"type":"date"}
        )
    )
    class Meta:
        model = Emprestimo
        fields = ['nome', 'email', 'data_retirada', 'data_devolucao']        
        
        