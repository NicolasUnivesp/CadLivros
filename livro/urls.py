from django.urls import path
from . views import ListaLivroView, LivroCreateView, LivroUpdateView, LivroDeleteView


urlpatterns = [
    path('', ListaLivroView.as_view(), name='livro.index'),
    path('novo/', LivroCreateView.as_view(), name='livro.novo'),
    path('editar/<int:pk>', LivroUpdateView.as_view(), name='livro.editar'),
    path('remover/<int:pk>', LivroDeleteView.as_view(), name='livro.remover')
]
