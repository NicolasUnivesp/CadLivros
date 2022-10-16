from django.urls import path
from . views import ListaLivroView, LivroCreateView, LivroUpdateView, LivroDeleteView
from . import views

urlpatterns = [
    path('', ListaLivroView.as_view(), name='livro.index'),
    path('novo/', LivroCreateView.as_view(), name='livro.novo'),
    path('<int:pk>/editar', LivroUpdateView.as_view(), name='livro.editar'),
    path('<int:pk>/remover', LivroDeleteView.as_view(), name='livro.remover'),
    path('<int:pk>/emprestimos', views.emprestimo, name='livro.emprestimo'),
]
