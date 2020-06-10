from django.contrib.auth.forms import AuthenticationForm


class SignInForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass
