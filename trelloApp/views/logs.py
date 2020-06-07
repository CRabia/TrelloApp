from django.shortcuts import render
from django.views import View


class LoginView(View):
    template_name = 'logs/sign-in.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
