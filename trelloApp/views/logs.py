from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views import View

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


def logout_view(request):
    logout(request)
    return redirect('signin')


class SigninView(View):
    template_name = 'logs/sign-in.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return render(request, self.template_name, {'error': "Cet utilisateur n'existe pas."})

        return render(request, self.template_name, {'error': "Informations invalident"})


class SignupView(View):
    template_name = 'logs/sign-up.html'
    form = UserCreationForm()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form, 'error': ""})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)

        if User.objects.filter(username=request.POST['username']).exists():
            return render(request, self.template_name, {'form': self.form, 'error': "Cet utilisateur existe déjà."})

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            return redirect('signup')