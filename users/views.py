from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from . import models, forms
from . forms import LoginForm


def register_view(request):
    if request.method == 'POST':
        form = forms.WorkerProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = forms.WorkerProfileForm()
    return render(request, 'users/register.html', {'form': form})


def auth_login_view(request):
    error = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            workers = models.WorkerProfile.objects.filter(username=username)
            if not workers.exists():
                error = 'Неверное имя пользователя или пароль'
            else:
                worker = workers.first()  # берём первого
                from django.contrib.auth.hashers import check_password
                if check_password(password, worker.password):
                    request.session['worker_id'] = worker.id
                    return redirect('users:profile')
                else:
                    error = 'Неверное имя пользователя или пароль'
        else:
            error = 'Неверный ввод капчи или другие ошибки'
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form, 'error': error})



def auth_logout_view(request):
    request.session.flush()
    return redirect('users:login')


def profile_view(request):
    worker_id = request.session.get('worker_id')
    if not worker_id:
        return redirect('users:login')

    try:
        worker = models.WorkerProfile.objects.get(id=worker_id)
    except models.WorkerProfile.DoesNotExist:
        request.session.flush()
        return redirect('users:login')

    return render(request, 'users/profile.html', {'worker': worker})
