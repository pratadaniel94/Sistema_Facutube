from django.shortcuts import render
from core.forms import ContatoForm
from core.models import Curso
from django.contrib.auth.decorators import login_required
# Create your views here.

def entrar(request):
    contexto = {
        'form': LoginForm
    }
    return render(request, 'login.html', contexto)

@login_required(login_url="/entrar")
def aluno(request):
    return render(request, 'index.html')

@login_required(login_url="/entrar")
def professor(request):
    return render(request, 'index.html')


def index(request):
    contexto = {
        "cursos": Curso.objects.all()
    }

    return  render(request,"index.html", contexto)

def contato(request):
    if request.POST:
        form = ContatoForm(request)
        if form.is_valid():
            form.envia_email()
    else:
        form = ContatoForm()
    contexto = {
        "form": form
    }
    return render(request, 'contato.html', contexto)



def noticia(request):
    contexto = {}
    return render(request,'noticia.html', contexto)

def cursos(request):
    contexto = {}
    return render(request,'curso.html', contexto)

def marketing(request):
    contexto = {}
    return render(request,'marketing.html', contexto)

def blogger(request):
    contexto = {}
    return render(request,'blogger.html', contexto)

def desing(request):
    contexto = {}
    return render(request,'desing.html', contexto)

def publicidade(request):
    contexto = {}
    return render(request,'publicidade.html', contexto)

def esqueci(request):
    return render(request,'esqueci-senha.html')

