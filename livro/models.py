from email.policy import default
from django.db import models

class Livro(models.Model):
    titulo_completo = models.CharField(max_length=256)
    data_cadastro = models.DateField(null=True)
    emprestado = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.titulo_completo



# camada de dados, ela representa a modelagem do objeto e como a tabela sera criada no banco de dados (sqlite)
