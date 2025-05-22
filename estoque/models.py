from django.db import models
from django.contrib.auth.models import User

class Livro(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    paginas = models.IntegerField()
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    imagem = models.ImageField(upload_to='livros/', null=True, blank=True)
    
    def __str__(self):
        return self.titulo
    
class SolicitacaoTroca(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    solicitante = models.ForeignKey(User, on_delete=models.CASCADE)
    mensagem = models.TextField(blank=True)
    data = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pendente')  

    def __str__(self):
        return f"{self.solicitante.username} quer trocar {self.livro.titulo}"



