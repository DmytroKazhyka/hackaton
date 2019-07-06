from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import DetailView, CreateView
from .models import Player


class PlayerDetailView(DetailView):
    template_name = 'player/profile.html'
    model = Player
    context_object_name = 'player'
    pk_url_kwarg = 'player_id'


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        # Create user
        created_user = form.save()
        # Create profile
        player = Player.objects.create(player=created_user)
        # Authenticate User
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password1'),
        )
        login(self.request, authenticated_user)
        return redirect('player', player.id)

