from pyexpat import model
from django import forms
from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    data_cadastro = forms.DateField(
        widget=forms.TextInput(
            attrs={"type":"date"}
        )
    )
    class Meta:
        model = Livro
        fields = ['titulo_completo', 'data_cadastro', 'emprestado']
        