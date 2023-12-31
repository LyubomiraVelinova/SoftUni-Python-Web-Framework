from django import forms
from django.urls import reverse_lazy
from django.views import generic as views
# from django import views
from django.shortcuts import render
from django.contrib.auth import views as auth_views, login, get_user_model
from django.contrib.auth import forms as auth_forms
from django.utils.translation import gettext_lazy as _


# Create your views here.

def register_user(request):
    pass


class RegisterUserForm(auth_forms.UserCreationForm):
    content = forms.BooleanField()
    password2 = forms.CharField(
        label=_("Repeat password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Repeat password, please"),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'It works'


class RegisterUserView(views.CreateView):
    template_name = 'app_auth/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('register_user')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class LoginUserView(auth_views.LoginView):
    template_name = "app_auth/login.html"


class LogoutUserView(views.View):
    pass


UserModel = get_user_model()


class UsersListView(views.ListView):
    model = UserModel
    template_name = 'app_auth/users_list.html'
