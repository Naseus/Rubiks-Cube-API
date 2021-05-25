from django.contrib import admin
from .models import Algorithm, Alternative, SolveTime

# Register your models here.

admin.site.register(Algorithm)
admin.site.register(Alternative)
admin.site.register(SolveTime)
