from django.db import models

# Create your models here.
class Curso(models.Model):
    sigla = models.CharField(unique=True, max_length=5)
    nome = models.CharField(unique=True, max_length=50)
    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'curso'

'''class Cursoturma(models.Model):
    id_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso')
    id_da_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_da_turma')
    sigla_curso = models.CharField(max_length=5)
    nome_disciplina = models.CharField(max_length=240, blank=True, null=True)
    ano_ofertado = models.SmallIntegerField()
    semestre_ofertado = models.CharField(max_length=1)
    id_turma = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cursoturma'
        unique_together = (('sigla_curso', 'nome_disciplina', 'ano_ofertado', 'semestre_ofertado', 'id_turma'),)

class Disciplina(models.Model):
    nome = models.CharField(unique=True, max_length=240)
    carga_horaria = models.SmallIntegerField()
    teoria = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    pratica = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    ementa = models.TextField(blank=True, null=True)
    competencia = models.TextField(blank=True, null=True)
    habilidades = models.TextField(blank=True, null=True)
    conteudo = models.TextField(blank=True, null=True)
    bibliografia_basica = models.TextField(blank=True, null=True)
    bibliografia_complementar = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disciplina'

class Disciplinaofertada(models.Model):
    id_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='id_disciplina')
    nome_disciplina = models.CharField(max_length=240)
    ano = models.SmallIntegerField()
    semestre = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'disciplinaofertada'
        unique_together = (('nome_disciplina', 'ano', 'semestre'),)

class Gradecurricular(models.Model):
    id_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso')
    sigla_curso = models.CharField(max_length=5)
    ano = models.SmallIntegerField()
    semestre = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'gradecurricular'
        unique_together = (('sigla_curso', 'ano', 'semestre'),)

class Periodo(models.Model):
    id_grade = models.ForeignKey(Gradecurricular, models.DO_NOTHING, db_column='id_grade')
    sigla_curso = models.CharField(max_length=5)
    ano_grade = models.SmallIntegerField()
    semestre_grade = models.CharField(max_length=1)
    numero = models.SmallIntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'periodo'
        unique_together = (('sigla_curso', 'ano_grade', 'semestre_grade'),)

class Periododisciplina(models.Model):
    id_periodo = models.ForeignKey(Periodo, models.DO_NOTHING, db_column='id_periodo')
    id_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='id_disciplina')
    sigla_curso = models.CharField(max_length=5, blank=True, null=True)
    ano_grade = models.SmallIntegerField()
    semestre_grade = models.CharField(max_length=1, blank=True, null=True)
    numero_periodo = models.SmallIntegerField()
    nome_disciplina = models.CharField(max_length=240)

    class Meta:
        managed = False
        db_table = 'periododisciplina'
        unique_together = (('sigla_curso', 'ano_grade', 'semestre_grade', 'numero_periodo', 'nome_disciplina'),)

class Aluno(models.Model):
    id_curso = models.ForeignKey('Curso', models.DO_NOTHING, db_column='id_curso')
    ra = models.IntegerField(unique=True)
    nome = models.CharField(max_length=120)
    email = models.CharField(max_length=80)
    celular = models.CharField(max_length=11)
    sigla_curso = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'aluno'

class Matricula(models.Model):
    id_aluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='id_aluno')
    id_da_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_da_turma')
    ra_aluno = models.IntegerField()
    nome_disciplina = models.CharField(max_length=240)
    ano_ofertado = models.SmallIntegerField()
    semestre_ofertado = models.CharField(max_length=1, blank=True, null=True)
    id_turma = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'matricula'
        unique_together = (('ra_aluno', 'nome_disciplina', 'ano_ofertado', 'semestre_ofertado', 'id_turma'),)

class Arquivoresposta(models.Model):
    id_resposta = models.ForeignKey('Resposta', models.DO_NOTHING, db_column='id_resposta')
    nome_disciplina = models.CharField(max_length=240)
    ano_ofertado = models.SmallIntegerField()
    semestre_ofertado = models.CharField(max_length=1)
    id_turma = models.CharField(max_length=1)
    numero_questao = models.IntegerField()
    ra_aluno = models.IntegerField()
    arquivo = models.CharField(unique=True, max_length=500)

    class Meta:
        managed = False
        db_table = 'arquivoresposta'
        unique_together = (('nome_disciplina', 'ano_ofertado', 'semestre_ofertado', 'id_turma', 'numero_questao', 'ra_aluno'),)

class Arquivosquestao(models.Model):
    id_questao = models.ForeignKey('Questao', models.DO_NOTHING, db_column='id_questao')
    nome_disciplina = models.CharField(max_length=240)
    ano_ofertado = models.SmallIntegerField()
    semestre_ofertado = models.CharField(max_length=1)
    id_turma = models.CharField(max_length=1)
    numero_questao = models.IntegerField()
    arquivo = models.CharField(unique=True, max_length=500)

    class Meta:
        managed = False
        db_table = 'arquivosquestao'
        unique_together = (('nome_disciplina', 'ano_ofertado', 'semestre_ofertado', 'id_turma', 'numero_questao'),)

class Professor(models.Model):
    ra = models.IntegerField(unique=True)
    apelido = models.CharField(unique=True, max_length=30)
    nome = models.CharField(max_length=120)
    email = models.CharField(max_length=80)
    celular = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'professor'

class Turma(models.Model):
    id_disciplinaofertada = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='id_disciplinaofertada')
    id_professor = models.ForeignKey(Professor, models.DO_NOTHING, db_column='id_professor')
    nome_disciplina = models.CharField(max_length=240, blank=True, null=True)
    ano_ofertado = models.SmallIntegerField()
    semestre_ofertado = models.CharField(max_length=1)
    id_turma = models.CharField(max_length=1)
    turno = models.CharField(max_length=15)
    ra_professor = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'turma'
        unique_together = (('nome_disciplina', 'ano_ofertado', 'semestre_ofertado'),)

class Questao(models.Model):
    id_da_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_da_turma')
    nome_disciplina = models.CharField(max_length=240)
    ano_ofertado = models.SmallIntegerField()
    semestre_ofertado = models.CharField(max_length=1)
    id_turma = models.CharField(max_length=1)
    numero = models.IntegerField(unique=True)
    data_limite_entrega = models.DateField()
    descricao = models.TextField(blank=True, null=True)
    data_questao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questao'
        unique_together = (('nome_disciplina', 'ano_ofertado', 'semestre_ofertado', 'id_turma'),)


class Resposta(models.Model):
    id_questao = models.ForeignKey(Questao, models.DO_NOTHING, db_column='id_questao')
    id_aluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='id_aluno')
    nome_disciplina = models.CharField(max_length=240)
    ano_ofertado = models.SmallIntegerField()
    semestre_ofertado = models.CharField(max_length=1)
    id_turma = models.CharField(max_length=1)
    numero_questao = models.IntegerField()
    ra_aluno = models.IntegerField(unique=True)
    data_avaciacao = models.DateField()
    nota = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    avalicao = models.TextField()
    descricao = models.TextField()
    data_de_envio = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resposta'
        unique_together = (('nome_disciplina', 'ano_ofertado', 'semestre_ofertado', 'id_turma', 'numero_questao'),)

'''
'''class Curso(models.Model):
    sigla = models.CharField(max_length=5)
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50, blank=True)
    carga_horaria = models.IntegerField(default=1000)
    ativo = models.BooleanField(default=False)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome'''

    