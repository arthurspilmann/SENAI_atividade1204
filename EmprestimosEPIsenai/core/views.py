from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ColaboradorForm, EPIForm, EmprestimoForm, RelatorioForm, FiltroEmprestimoForm
from .models import Colaborador, EPI, Emprestimo
from django.contrib import messages


@login_required
def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'erro': 'Usuário ou senha inválidos'})
    return render(request, 'login.html')

@login_required
def editar_epi_view(request, epi_id):
    epi = get_object_or_404(EPI, pk=epi_id)
    form = EPIForm(request.POST or None, instance=epi)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, '✅ EPI atualizado com sucesso!')
            return redirect('epis')
        else:
            messages.error(request, '❌ Erro ao atualizar EPI.')

    epis = EPI.objects.all()
    return render(request, 'epis.html', {'form': form, 'epis': epis, 'epi_id': epi.id})

@login_required
def excluir_epi_view(request, epi_id):
    epi = get_object_or_404(EPI, pk=epi_id)
    epi.delete()
    messages.success(request, '🗑️ EPI excluído com sucesso!')
    return redirect('epis')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def colaboradores_view(request, colaborador_id=None):
    if colaborador_id:
        colaborador = get_object_or_404(Colaborador, pk=colaborador_id)
        form = ColaboradorForm(request.POST or None, instance=colaborador)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, '✅ Colaborador atualizado com sucesso!')
                return redirect('colaboradores')
            else:
                messages.error(request, '❌ Erro ao atualizar colaborador.')
    else:
        form = ColaboradorForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, '✅ Colaborador cadastrado com sucesso!')
                return redirect('colaboradores')
            else:
                messages.error(request, '❌ Erro ao cadastrar colaborador.')

    colaboradores = Colaborador.objects.all()
    return render(request, 'colaboradores.html', {
        'form': form,
        'colaboradores': colaboradores,
        'colaborador_id': colaborador_id
    })

@login_required
def epis_view(request):
    form = EPIForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, '✅ EPI cadastrado com sucesso!')
            return redirect('epis')
        else:
            messages.error(request, '❌ Erro ao cadastrar EPI. Verifique os dados.')

    epis = EPI.objects.all()
    return render(request, 'epis.html', {'form': form, 'epis': epis})

@login_required
def emprestimos_view(request):
    form = EmprestimoForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Empréstimo registrado com sucesso!')
            return redirect('emprestimos')
        else:
            messages.error(request, '❌ Erro ao registrar empréstimo. Verifique os dados.')

    emprestimos = Emprestimo.objects.all()
    return render(request, 'emprestimos.html', {'form': form, 'emprestimos': emprestimos})


@login_required
def excluir_colaborador_view(request, colaborador_id):
    colaborador = get_object_or_404(Colaborador, pk=colaborador_id)
    colaborador.delete()
    messages.success(request, '🗑️ Colaborador excluído com sucesso!')
    return redirect('colaboradores')

@login_required
def relatorio_view(request):
    form = FiltroEmprestimoForm(request.POST or None)
    emprestimos = Emprestimo.objects.all()

    if request.method == 'POST':
        if form.is_valid():
            nome = form.cleaned_data.get('nome_colaborador')
            if nome:
                emprestimos = emprestimos.filter(colaborador__nome__icontains=nome)

    return render(request, 'relatorio.html', {'form': form, 'emprestimos': emprestimos})