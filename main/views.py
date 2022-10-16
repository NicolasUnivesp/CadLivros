from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'main/index.html'







# criar metodo responsavel por renderizar par ao usuario
# intermedio de dados e front.
