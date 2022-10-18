from django.contrib import admin
from .models import Livro, Emprestimo


# Register your models here.
class LivroAdmin(admin.ModelAdmin):
    list_display = [
        'titulo_completo',
        'data_cadastro',
        'emprestado'
    ]
    list_filter = [
        'emprestado',
        'data_cadastro'
    ]
    search_fields = [
        'titulo_completo'        
    ] 
    
admin.site.register(Livro, LivroAdmin)
admin.site.register(Emprestimo)