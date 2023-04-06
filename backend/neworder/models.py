from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save

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
    
class Users(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.user.username + ' / ' + self.name

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)




