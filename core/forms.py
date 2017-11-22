from core.models import Curso
from django import forms
from django.contrib.auth.admin import UserAdmin

class FormCurso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = "__all__"

class ContatoForm(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    # assunto = forms.
    mensagem = forms.CharField()

    def envia_email(self):
        print(
            "Email enviado para você: \n"+
            "Aluno: "+self.cleaned_data["nome"]+"\n"+
            "Email: "+self.cleaned_data["email"]+"\n"+
            "Mensagem : "+self.cleaned_data['mensagem']
        )

'''class NovoAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('ra','email', 'nome','curso')
    def save(self, commit=True):
        user = super(NovoAlunoForm, self).save(commit=False)
        user.set_password('123@mudar')
        user.perfil = 'A'
        if commit:
            user.save()
        return user

class AlterarAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('email', 'nome', 'curso')
            
class AlunoAdmin(UserAdmin):
    form = AlterarAlunoForm
    add_form = NovoAlunoForm'''