from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Permission, Group

class Category(models.Model):

    name = models.CharField(max_length=250, help_text = ("Selecione a categoria da ordem de serviço"))
    

    def __str__(self):
        return self.name

class RealStateAgency(models.Model):

    name = models.CharField(max_length=250, help_text = ("Selecione a Imobiliária"))
    

    def __str__(self):
        return self.name

class Company(models.Model):

    name = models.CharField(max_length=250, help_text = ("Selecione a companhia"))
    

    def __str__(self):
        return self.name

class Order(models.Model):
    contact_name = models.CharField(max_length=250)
    contact_phone = models.IntegerField()
    real_state = models.ForeignKey(RealStateAgency, on_delete=models.PROTECT, null=True, blank=True) 
    order_description = models.TextField(max_length=1000)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True) 
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)  
    deadline = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.contact_name
    



class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Cria e salva um usuário com o e-mail e senha especificados.
        """
        if not email:
            raise ValueError('O endereço de e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Cria e salva um superusuário com o e-mail e senha especificados.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    groups = models.ManyToManyField(
        Group, related_name='neworder_users', blank=True,
        help_text='Os grupos aos quais o usuário pertence. '
                  'Um usuário terá todos os privilégios e permissões atribuídos '
                  'a cada um dos seus grupos.',
    )
    user_permissions = models.ManyToManyField(
        Permission, related_name='neworder_users', blank=True,
        help_text='Específico às permissões deste usuário.',
        verbose_name='permissões do usuário',
    )

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

from django.contrib.auth import get_user_model

UserModel = get_user_model()


class EmailBackend:
    """
    Autentica usuários com base no endereço de e-mail e senha.
    """
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
