from django.contrib import admin
from .models import Type, Program, ProgramComment

admin.site.register(Type)
admin.site.register(Program)
admin.site.register(ProgramComment)