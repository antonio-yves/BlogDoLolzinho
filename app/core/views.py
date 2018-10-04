from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from django.urls import reverse_lazy

from . import models

from .forms import RegistrationUserForm

class UserCreateView(CreateView):
    model = models.UUIDUser
    template_name = 'core/cadastro.html'
    success_url = reverse_lazy('core:login')
    form_class = RegistrationUserForm

    def form_valid(self, form):
    	obj = form.save(commit=False)
    	obj.set_password(obj.password)
    	obj.save()
    	return super(UserCreateView, self).form_valid(form)

