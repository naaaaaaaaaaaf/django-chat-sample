from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CreateRoomForm
from .models import Room

class HomeView(generic.TemplateView):
    template_name = 'home.html'

class RoomCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'room/create.html'
    form_class = CreateRoomForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)
    
class RoomListView(generic.ListView):
    template_name = 'room/list.html'
    model = Room