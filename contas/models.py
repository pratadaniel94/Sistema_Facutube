from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        UserManager, models)

# Create your models here.  

class UsuarioManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, ra, password, **extra_fields):
        if not ra:
            raise ValueError("RA precisa ser preenchido")
        user = self.model(ra=ra, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, ra, password, **extra_fields):
        return self._create_user(ra, password, **extra_fields)
    def create_superuser(self, ra, password, **extra_fields):
        return self._create_user(ra, password, **extra_fields)

#criando o Modelo de 'USUARIO'
class Usuario(AbstractBaseUser):
    ra = models.IntegerField('RA', unique=True)
    nome = models.CharField(max_length=120)
    email = models.CharField(max_length=80)
    password = models.TextField()
    status = models.BooleanField('Status', default=True)
    perfil = models.CharField('Perfil', max_length=1, default='C')   

    # criando qual o campo de identificação do 'USUARIO'
    USERNAME_FIELD = 'ra'

    #colocando com campo de inserção obrigatorio no 'BANCO'
    REQUIRED_FIELDS = ['nome','email',]

    objects = UsuarioManager()

    # criando a função de apresentação do 'USUARIO'
    def __str__(self):
        return self.nome

    # criando as funcoes de como ira mostra o nome do 'USUARIO' nos Templates
    
    #  Funções 'OBRIGATORIAS pelo DJANGO
    def get_full_name(self):
        return self.nome

    def get_short_name(self):
        return self.nome

    def has_perm(self, perm,obj=None):
        return True
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.perfil == 'C'
    
class Aluno(AbstractBaseUser):
    nome = models.CharField(max_length=120)
    ra = models.IntegerField(unique=True)
    password = models.TextField()
    status = models.BooleanField(default=True)
    email = models.CharField(max_length=80, blank=True, null=True)
    perfil = models.CharField(max_length=1, blank=True, default='A')
    celular = models.CharField(max_length=11, blank=True, null=True)

    USERNAME_FIELD = 'ra'
    REQUIRED_FIELDS = ['nome','email']

    def __str__(self):
        return self.nome + '(' + str(self.ra) + ')'
    class Meta:
        managed = False
        db_table = 'aluno'


class Professor(AbstractBaseUser):
    nome = models.CharField(max_length=120)
    ra = models.IntegerField(unique=True)
    password = models.TextField()
    status = models.BooleanField(default=True)
    email = models.CharField(max_length=80, blank=True, null=True)
    perfil = models.CharField(max_length=1, blank=True, default='P')
    celular = models.CharField(max_length=11, blank=True, null=True)

    USERNAME_FIELD = 'ra'
    REQUIRED_FIELDS = ['nome','email']

    def __str__(self):
        return self.nome + '(' + str(self.ra) + ')'
    class Meta:
        managed = False
        db_table = 'professor'

    
        