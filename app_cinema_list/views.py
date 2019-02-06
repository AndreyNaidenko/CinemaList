from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Cinema


def index(request):
    film = get_object_or_404(Cinema)
    return render(request, 'app_cinema_list/main.html', {'context': film})
