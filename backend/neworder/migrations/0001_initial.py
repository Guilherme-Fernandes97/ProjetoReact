# Generated by Django 4.1.5 on 2023-01-30 20:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Selecione a categoria da ordem de serviço', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Selecione a companhia', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='RealStateAgency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Selecione a Imobiliária', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=250)),
                ('contact_phone', models.IntegerField()),
                ('order_description', models.TextField(max_length=1000)),
                ('deadline', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='neworder.category')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='neworder.company')),
                ('real_state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='neworder.realstateagency')),
            ],
        ),
    ]
