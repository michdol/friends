from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import FormView

from users.forms import CreateUserForm, LoginForm


class CreateUserView(FormView):
    template_name = 'users/registration.html'
    form_class = CreateUserForm
    success_url = 'users/profile/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = 'users:profile'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        print("username", username)
        print("password", password)
        user = authenticate(self.request, username=username, password=password)
        print("user", user)
        if user:
            login(self.request, user)
            return HttpResponseRedirect(reverse(self.success_url))
        else:
            return self.get(self.request)


class Profile(TemplateView):
    template_name = 'users/profile.html'


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))
