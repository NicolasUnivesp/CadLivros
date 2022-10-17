from django.urls import path
from . views import ListaLivroView, LivroCreateView, LivroUpdateView, LivroDeleteView
from . import views

urlpatterns = [
    # classes:
    path('', ListaLivroView.as_view(), name='livro.index'),
    path('novo/', LivroCreateView.as_view(), name='livro.novo'),
    path('<int:pk>/editar', LivroUpdateView.as_view(), name='livro.editar'),
    path('<int:pk>/remover', LivroDeleteView.as_view(), name='livro.remover'),
    
    
    # metodos :
    path('<int:pk_livro>/emprestimo', views.emprestimo, name='livro.emprestimo'),
    path('<int:pk_livro>/emprestimo/novo', views.emprestimo_novo, name='emprestimo.novo'),
    path('<int:pk_livro>/emprestimo/<int:pk>/editar', views.emprestimo_editar, name='emprestimo.editar'),
    path('<int:pk_livro>/emprestimo/<int:pk>/remover', views.emprestimo_remover, name='emprestimo.remover'),
    
]
