from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),  
    path('livro/novo/', views.cadastrar_livro, name='cadastrar_livro'),
    path('solicitacoes/', views.solicitacoes, name='solicitacoes'),
    path('solicitacao/<int:solicitacao_id>/excluir/', views.excluir_solicitacao, name='excluir_solicitacao'),
    path('cadastro/', views.cadastrar_usuario, name='cadastro'),
    path('livro/<int:id>/editar/', views.editar_livro, name='editar_livro'),
    path('livro/<int:id>/excluir/', views.excluir_livro, name='excluir_livro'),
    path('livro/<int:livro_id>/solicitar-troca/', views.solicitar_troca, name='solicitar_troca'),


]
