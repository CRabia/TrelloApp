from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import redirect, render
from django.views import View

from trelloApp.forms.signin import SignInForm
from trelloApp.forms.signup import SignUpForm
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User


def logout_view(request):
    logout(request)
    return redirect('login')


class SigninView(View):
    form_class = SignInForm
    template_name = 'logs/sign-in.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        print(user)
        print(request.POST['password'])
        print(check_password(request.POST['password'], user.password))
        if check_password(request.POST['password'], user.password):
            login(request, user)
            return redirect('home')
        else:
            return redirect('signin')
        

class SignupView(View):
    form_class = SignUpForm
    template_name = 'logs/sign-up.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = SignUpForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            if User.objects.filter(username=username).exists():
                response = {
                    "already_exist": True
                }
                return render(request, self.template_name, context=response)

            user = User.objects.create(username=username, email=username)
            user.set_password(raw_password=raw_password)
            user.save()
            user = authenticate(request, username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('signin')
        else:
            response = {
                "signup_error": True
            }
            return render(request, self.template_name, context=response)
