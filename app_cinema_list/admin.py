from django.contrib import admin
from .models import Cinema
from .models import Actor
from .models import Genre


admin.site.register(Cinema)
admin.site.register(Actor)
admin.site.register(Genre)
