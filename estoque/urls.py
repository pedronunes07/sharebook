#from django.urls import path
#from . import views
#from .views import cadastrar_usuario

#urlpatterns = [ 
#    path('', views.lista_livros_disponiveis, name='index'),
#    path('adicionar/', views.adicionar_livro, name='adicionar_livro'),
#    path('editar/<int:id>/', views.editar_livro, name='editar_livro'),
#    path('excluir/<int:id>/', views.excluir_livro, name='excluir_livro'),
#    path('cadastrar/', views.cadastrar_livro, name='cadastrar_livro'),
#    path('cadastro/', cadastrar_usuario, name='cadastro'),
#]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),  
    path('livro/novo/', views.cadastrar_livro, name='cadastrar_livro'),
    path('cadastro/', views.cadastrar_usuario, name='cadastro'),
    path('livro/<int:id>/editar/', views.editar_livro, name='editar_livro'),
    path('livro/<int:id>/excluir/', views.excluir_livro, name='excluir_livro'),
    path('livro/<int:livro_id>/solicitar-troca/', views.solicitar_troca, name='solicitar_troca'),


]
