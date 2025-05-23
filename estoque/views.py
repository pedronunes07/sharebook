from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm, LivroForm
from .models import Livro, SolicitacaoTroca

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
        livro = Livro()
        livro.titulo = request.POST.get('titulo')
        livro.autor = request.POST.get('autor')
        livro.paginas = request.POST.get('paginas')
        livro.preco = request.POST.get('preco')
        livro.usuario = request.user
        
        if 'imagem' in request.FILES:
            livro.imagem = request.FILES['imagem']
            
        livro.save()
        return redirect('index')  

    return render(request, 'cadastrar_livro.html')

@login_required
def editar_livro(request, id):
    livro = get_object_or_404(Livro, id=id, usuario=request.user)

    if request.method == 'POST':
        livro.titulo = request.POST.get('titulo')
        livro.autor = request.POST.get('autor')
        livro.paginas = request.POST.get('paginas')
        livro.preco = request.POST.get('preco')
        
        if 'imagem' in request.FILES:
            livro.imagem = request.FILES['imagem']
            
        livro.save()
        return redirect('home')

    return render(request, 'editar_livro.html', {'livro': livro})

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
        return redirect('index')  

    if request.method == 'POST':
        mensagem = request.POST.get('mensagem', '')
        SolicitacaoTroca.objects.create(
            livro=livro,
            solicitante=request.user,
            mensagem=mensagem
        )
        return redirect('solicitacoes')
    
    return render(request, 'solicitar_troca.html', {
        'livro': livro
    })

@login_required
def solicitacoes(request):
    
    solicitacoes_recebidas = SolicitacaoTroca.objects.filter(livro__usuario=request.user)
    
    solicitacoes_enviadas = SolicitacaoTroca.objects.filter(solicitante=request.user)
    
    return render(request, 'solicitacoes.html', {
        'solicitacoes_recebidas': solicitacoes_recebidas,
        'solicitacoes_enviadas': solicitacoes_enviadas
    })

@login_required
def excluir_solicitacao(request, solicitacao_id):
    solicitacao = get_object_or_404(SolicitacaoTroca, id=solicitacao_id)
    
  
    if solicitacao.livro.usuario != request.user and solicitacao.solicitante != request.user:
        return redirect('solicitacoes')
        
    if request.method == 'POST':
        solicitacao.delete()
        return redirect('solicitacoes')
    
    return render(request, 'excluir_solicitacao.html', {'solicitacao': solicitacao})

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


