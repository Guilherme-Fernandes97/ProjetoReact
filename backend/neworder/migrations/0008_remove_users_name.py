# Generated by Django 4.1.5 on 2023-04-06 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neworder', '0007_remove_users_birth_date_remove_users_cpf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='name',
        ),
    ]
