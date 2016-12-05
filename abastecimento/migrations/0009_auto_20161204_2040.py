# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-04 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abastecimento', '0008_auto_20161204_1939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemmanutencaoveiculo',
            name='tempoServico',
        ),
        migrations.AddField(
            model_name='itemmanutencaoveiculo',
            name='status',
            field=models.BooleanField(choices=[(False, 'N\xe3o'), (True, 'Sim')], default=False, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='itemmanutencaoveiculo',
            name='valorAcumulado',
            field=models.IntegerField(default=0, verbose_name='Horas ou Kilometros ja registrado'),
        ),
        migrations.AlterField(
            model_name='itemmanutencaoveiculo',
            name='quantidade',
            field=models.IntegerField(default=0, verbose_name='Quantidade de itens'),
        ),
    ]