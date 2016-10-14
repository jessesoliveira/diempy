# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-29 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nome', models.CharField(db_column='Nome', max_length=255)),
                ('unidade', models.CharField(db_column='Unidade', max_length=100)),
                ('cod_curso', models.CharField(db_column='Cod_Curso', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'cursos',
                'verbose_name': 'curso',
                'managed': False,
                'ordering': ('-id',),
                'db_table': 'Curso',
            },
        ),
        migrations.CreateModel(
            name='PessoaCurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(db_column='Matricula', max_length=100)),
            ],
            options={
                'db_table': 'Pessoa__Curso',
                'managed': False,
            },
        ),
    ]