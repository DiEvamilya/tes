from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm

def auth_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None:
                login(request, user)
                messages.add_message(request, messages.WARNING, 'Аутентификация прошла успешно')
                return redirect('category_list')  # Предполагается, что у вас есть страница после успешного входа
            else:
                messages.add_message(request, messages.WARNING, 'Неверные данные')
                return render(request, 'auth_users/login.html', {'form': form, 'error': 'Неверные данные'})

    else:
        form = LoginForm()
        messages.add_message(request, messages.WARNING, 'Не удалось выполнить аутентификацию')
    return render(request, 'auth_users/login.html', {'form': form})



def auth_logout(request):
    logout(request)
    return redirect('auth_login')