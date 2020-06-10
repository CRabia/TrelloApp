from django import forms


class SignUpForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.PasswordInput()
