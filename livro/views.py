from django.http import HttpResponse, Http404
from django.http.response import HttpResponseNotAllowed
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Emprestimo, Livro
from .forms import LivroForm, EmprestimoForm



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


def emprestimo(request, pk_livro):
    emprestimo = Emprestimo.objects.filter(livro=pk_livro)
    return render(request, 'emprestimo/emprestimo_list.html', {'emprestimos': emprestimo, 'pk_livro': pk_livro})#

def emprestimo_novo(request, pk_livro):
    form = EmprestimoForm()
    if request.method == "POST":
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            emprestimo.livro_id = pk_livro;
            emprestimo.save()
            return redirect(reverse('livro.emprestimo', args=[pk_livro]))
    return render(request, 'emprestimo/emprestimo_form.html', {'form': form})

def emprestimo_editar(request, pk_livro, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    form = EmprestimoForm(instance=emprestimo)
    if request.method == "POST":
        form = EmprestimoForm(request.POST, instance=emprestimo)
        if form.is_valid():
            form.save()
            return redirect(reverse('livro.emprestimo', args=[pk_livro]))
    return render(request, 'emprestimo/emprestimo_form.html', {'form':form})    

def emprestimo_remover(request, pk_livro, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    emprestimo.delete()
    return redirect(reverse('livro.emprestimo', args=[pk_livro]))
    # return redirect(reverse('livro.emprestimo', args=[pk_livro]))

    


# Create your views here.


