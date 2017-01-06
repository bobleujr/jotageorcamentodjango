# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('codigo', models.AutoField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=1000)),
                ('cnpj', models.CharField(max_length=100)),
                ('informacoes_adicionais', models.CharField(max_length=2000)),
                ('descricacao', models.CharField(max_length=5000)),
                ('endereco', models.CharField(max_length=1000)),
                ('numero', models.IntegerField()),
                ('cep', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=100)),
                ('fax', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('codigo', models.AutoField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=1000)),
                ('cnpj', models.CharField(max_length=100)),
                ('informacoes_adicionais', models.CharField(max_length=2000)),
                ('descricacao', models.CharField(max_length=5000)),
                ('endereco', models.CharField(max_length=1000)),
                ('numero', models.IntegerField()),
                ('cep', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=100)),
                ('fax', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Orcamento',
            fields=[
                ('codigo', models.AutoField(serialize=False, primary_key=True)),
                ('descricacao', models.CharField(max_length=5000)),
                ('cliente', models.ForeignKey(to='orcamento.Cliente')),
                ('empresa_jotage', models.ForeignKey(to='orcamento.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='OrcamentoXProduto',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('quantidade', models.IntegerField()),
                ('preco_adaptavel', models.DecimalField(max_digits=10, decimal_places=2)),
                ('orcamento', models.ForeignKey(to='orcamento.Orcamento')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('codigo', models.AutoField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=1000)),
                ('descricacao', models.CharField(max_length=5000)),
                ('preco_jotage', models.DecimalField(max_digits=10, decimal_places=2)),
                ('preco_banda_ativa', models.DecimalField(max_digits=10, decimal_places=2)),
                ('preco_adicional', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.AddField(
            model_name='orcamentoxproduto',
            name='produto',
            field=models.ForeignKey(to='orcamento.Produto'),
        ),
    ]
