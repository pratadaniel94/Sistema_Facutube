from django.contrib import admin
# from contas.models import Aluno, Professor, Coordenador
from django.contrib.auth.admin import UserAdmin
from contas.models import Aluno, Professor

from contas.forms import novo_aluno_form
from contas.forms import novo_professor_form

# Register your models here.
class Cadastro_Admin(UserAdmin):
    add_form = novo_aluno_form
    list_display = ('email', 'nome')
    list_filter = ('perfil',)
    fieldsets = ( (None, {'fields': ('ra','email', 'nome')}),)
    add_fieldsets = ((None, { 'fields': ('ra', 'email', 'nome')} ),)
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(Aluno, Cadastro_Admin)
admin.site.register(Professor, Cadastro_Admin)
