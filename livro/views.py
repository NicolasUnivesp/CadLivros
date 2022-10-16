from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Livro
from .forms import LivroForm

class ListaLivroView(ListView):
    model = Livro
    queryset = Livro.objects.all().order_by('titulo_completo')
    
    def get_queryset(self):
        queryset = super().get_queryset()
        filtro_titulo = self.request.GET.get('titulo') or None
        
        if filtro_titulo:
            queryset = queryset.filter(titulo_completo__contains=filtro_titulo)
        return queryset
    

class LivroCreateView(CreateView):
    model = Livro
    form_class = LivroForm
    success_url = '/livros/'
    
class LivroUpdateView(UpdateView):
    model = Livro
    form_class = LivroForm
    success_url = '/livros/'

class LivroDeleteView(DeleteView):
    model = Livro
    success_url = '/livros/'

# Create your views here.
