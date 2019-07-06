from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from player.views import PlayerDetailView, SignUp
from guess_number.views import start_game

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('player/profile/<int:player_id>', PlayerDetailView.as_view(), name='player'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('start_game/', start_game, name='start_game')
]
