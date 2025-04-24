from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm

@login_required
def home(request):
    livros = Livro.objects.filter(usuario=request.user)
    return render(request, 'estoque/home.html', {'livros': livros})

def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'lista_livros.html', {'livros': livros})

def adicionar_livro(request):
    form = LivroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_livros')
    return render(request, 'form_livro.html', {'form': form})

def editar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    form = LivroForm(request.POST or None, instance=livro)
    if form.is_valid():
        form.save()
        return redirect('lista_livros')
    return render(request, 'form_livro.html', {'form': form})

def excluir_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    if request.method == "POST":
        livro.delete()
        return redirect('lista_livros')
    return render(request, 'confirmar_exclusao.html', {'livro': livro})

@login_required
def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            livro = form.save(commit=False)
            livro.usuario = request.user
            livro.save()
            return redirect('home')  # Ou outro lugar
    else:
        form = LivroForm()
    return render(request, 'estoque/cadastrar_livro.html', {'form': form})

def lista_livros_disponiveis(request):
    livros = Livro.objects.all()  # você pode filtrar por disponibilidade se quiser
    return render(request, 'index.html', {'livros': livros})

def form_valid(self, form):
    form.instance.usuario = self.request.user
    return super().form_valid(form)


def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # redireciona pro login após cadastro
    else:
        form = UsuarioForm()
    return render(request, 'cadastrar_usuario.html', {'form': form})