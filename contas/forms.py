from django import forms
from contas.models import Aluno, Professor
from django.contrib.auth.admin import UserAdmin
# --------------------------------------------------------/ Aluno /----------------------------------------------------------------------
# criando o Formilario de 'USUARIO'/'ALUNO'

class novo_aluno_form(forms.ModelForm):

    class meta:
        model = Aluno
        fields = ('ra','email','nome')

    def save(self,commit=True):
        user = super(novo_aluno_form,self).save(commit=False)
        user.set_password('123@mudar')
        if commit:
            user.save()
        return user

class altera_aluno_form(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = ('email','nome')

class aluno_admin(UserAdmin):
    form = altera_aluno_form
    add_form = novo_aluno_form

# --------------------------------------------------------/ Professor /----------------------------------------------------------------------
# criando o Formilario de 'USUARIO'/'PROFESSOR'
class novo_professor_form(forms.ModelForm):

    class meta:
        model = Professor
        fields = ('ra','email','nome')
    def save(self,commit=True):
        user = super(novo_professor_form,self).save(commit=False)
        user.set_password('123@mudar')
        if commit:
            user.save()
        return user
class altera_professor_form(forms.ModelForm):

    class Meta:
        model = Professor
        fields = ('email','nome')
class professor_admin(UserAdmin):
    form = altera_professor_form
    add_form = novo_professor_form
