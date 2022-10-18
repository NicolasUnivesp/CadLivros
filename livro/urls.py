from django.urls import path
from . views import ListaLivroView, LivroCreateView, LivroUpdateView, LivroDeleteView
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    # classes:
    path('', login_required(ListaLivroView.as_view()), name='livro.index'),
    path('novo/', login_required(LivroCreateView.as_view()), name='livro.novo'),
    path('<int:pk>/editar', login_required(LivroUpdateView.as_view()), name='livro.editar'),
    path('<int:pk>/remover', login_required(LivroDeleteView.as_view()), name='livro.remover'),
    
    
    # metodos :
    path('<int:pk_livro>/emprestimo', login_required(views.emprestimo), name='livro.emprestimo'),
    path('<int:pk_livro>/emprestimo/novo', login_required(views.emprestimo_novo), name='emprestimo.novo'),
    path('<int:pk_livro>/emprestimo/<int:pk>/editar', login_required(views.emprestimo_editar), name='emprestimo.editar'),
    path('<int:pk_livro>/emprestimo/<int:pk>/remover', login_required(views.emprestimo_remover), name='emprestimo.remover'),
    
]
