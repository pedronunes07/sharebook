from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm, LivroForm
from .models import Livro

def index(request):
    livros = Livro.objects.all()
    return render(request, 'index.html', {'livros': livros})

@login_required
def home(request):
    livros = Livro.objects.filter(usuario=request.user)
    return render(request, 'home.html', {'livros': livros})

@login_required
def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            livro = form.save(commit=False)
            livro.usuario = request.user
            livro.save()
            return redirect('home')
    else:
        form = LivroForm()
    return render(request, 'cadastrar_livro.html', {'form': form})


@login_required
def editar_livro(request, id):
    livro = get_object_or_404(Livro, id=id, usuario=request.user)

    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LivroForm(instance=livro)

    return render(request, 'editar_livro.html', {'form': form, 'livro': livro})


@login_required
def excluir_livro(request, id):
    livro = get_object_or_404(Livro, id=id, usuario=request.user)

    if request.method == 'POST':
        livro.delete()
        return redirect('home')

    return render(request, 'excluir_livro.html', {'livro': livro})


@login_required
def solicitar_troca(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)

    if livro.usuario == request.user:
        return redirect('index')  # não pode solicitar troca com você mesmo

    if request.method == 'POST':
        mensagem = request.POST.get('mensagem', '')
        SolicitacaoTroca.objects.create(
            livro=livro,
            solicitante=request.user,
            mensagem=mensagem
        )
        return redirect('index')

    return render(request, 'solicitar_troca.html', {'livro': livro})



def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('home')
    else:
        form = UsuarioForm()
    return render(request, 'cadastrar_usuario.html', {'form': form})


