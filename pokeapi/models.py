from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Criar Usuários
class CriarUsuario(BaseUserManager):
    def criar_usuario(self, nome_usuario, email_usuario, senha_usuario=None, **extra_fields):
        if not email_usuario:
            raise ValueError('E-mail do usuário obrigatório')
        if not nome_usuario:
            raise ValueError('Nome do usuário obrigatório')
        email_usuario = self.normalize_email(email_usuario)
        usuario = self.model(email_usuario=email_usuario, nome_usuario=nome_usuario, **extra_fields)
        usuario.set_password(senha_usuario)
        usuario.save(using=self._db)
        return usuario

# Usuarios
class Usuarios(AbstractBaseUser, PermissionsMixin):
    email_usuario = models.EmailField(unique=True)
    nome_usuario = models.CharField(max_length=30, unique=True)
    esta_ativa = models.BooleanField(default=True)
    objects = CriarUsuario()
    USERNAME_FIELD = 'email_usuario'
    REQUIRED_FIELDS = ['nome_usuario']

    def __str__(self):
        return self.email_usuario

