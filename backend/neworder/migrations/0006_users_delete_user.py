# Generated by Django 4.1.5 on 2023-04-03 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('neworder', '0005_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('birth_date', models.DateField(help_text='Padrão DD/MM/AAAA. Exemplo: 15/10/1990', verbose_name='Data de Nascimento')),
                ('cpf', models.CharField(help_text='Somente números. Exemplo: 10020030050', max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]