# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-06 00:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abastecimento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='abastecimento',
            name='quantidade',
            field=models.FloatField(verbose_name='Quantidade'),
        ),
        migrations.AlterField(
            model_name='abastecimento',
            name='responsavel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abastecimento.Usuario'),
        ),
        migrations.AlterField(
            model_name='abastecimento',
            name='valor',
            field=models.FloatField(verbose_name='Valor'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='dono',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='abastecimento.Usuario'),
        ),
    ]