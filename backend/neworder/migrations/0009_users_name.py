# Generated by Django 4.1.5 on 2023-04-06 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neworder', '0008_remove_users_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='name',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
