from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CadastroForm, AddProdutoForm
from .models import Produto


def home(request):
    produtos = Produto.objects.all()

    if request.method == 'POST':
        user_nome = request.POST['username']
        user_senha = request.POST['password']
        user = authenticate(request, username = user_nome, password = user_senha)
        if user is not None:
            login (request, user)
            messages.success(request,"Bem vindo de volta!")
            return redirect('home')
        else:
            messages.success(request, "Alguma credencial está incorreta :(")
            return redirect('home')
    else:
        return render(request, 'home.html', {'produtos': produtos})

def logout_user(request):
    logout(request)
    messages.success(request, "Adeus! Volte sempre!")
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            user_nome = form.cleaned_data['username']
            user_senha = form.cleaned_data['password1']
            user = authenticate(request, username = user_nome, password = user_senha )
            login(request, user)
            messages.success(request, "Bem vindo!")
            return redirect('home')
    else:
        form = CadastroForm()
        return render(request, 'register.html',{'form': form})
    return render(request, 'register.html', {'form': form})

def cliente_produto(request, pk):
    if request.user.is_authenticated:
         produto = Produto.objects.get(id = pk)
         return render(request, 'produto.html', {'produto': produto})
    else:
        messages.success(request, "Você precisa estar logado para a visualizar")
        return redirect('home')
    
def deletar_produto(request, pk):
    if request.user.is_authenticated:
         produto_deletado = Produto.objects.get(id = pk)
         produto_deletado.delete()
         messages.success(request, "Produto deletado com sucesso")
         return redirect('home')
    else:
        messages.success(request, "Você precisa estar logado para a visualizar")
        return redirect('home')
    
def adicionar_produto(request):
    form = AddProdutoForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request,"Produto adicionado com sucesso")
                return redirect('home')
        return render(request, 'adicionar_produto.html', {'form': form})
    else:
        messages.success(request, "Você precisa estar logado para a visualizar")
        return redirect('home')

def editar_produto(request, pk):
    if request.user.is_authenticated:
        produto_atual = Produto.objects.get(id = pk)
        form = AddProdutoForm(request.POST or None, instance = produto_atual)
        if form.is_valid():
            form.save()
            messages.success(request, "O produto foi editado com sucesso")
            return redirect('home')
        return render(request, 'editar_produto.html', {'form': form})
    else:
        messages.success(request, "Você precisa estar logado para a visualizar")
        return redirect('home')


   

        
        

    
                       


    
