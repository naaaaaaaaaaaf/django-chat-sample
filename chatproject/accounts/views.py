from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from .forms import AccountCreationForm

class AccountRegisterView(CreateView):
    form_class = AccountCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'
