from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'front/home.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
            return render(request, self.template_name)
        else:
            return redirect('signin')
