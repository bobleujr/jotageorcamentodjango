from django.db import models

# Create your models here.


class Produto(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=1000)
    descricacao = models.CharField(max_length=5000)
    preco_jotage = models.DecimalField(max_digits=10, decimal_places=2)
    preco_banda_ativa = models.DecimalField(max_digits=10, decimal_places=2)
    preco_adicional = models.DecimalField(max_digits=10, decimal_places=2)



class Empresa(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=1000)
    cnpj = models.CharField(max_length=100)
    informacoes_adicionais = models.CharField(max_length=2000)
    descricacao = models.CharField(max_length=5000)
    endereco = models.CharField(max_length=1000)
    numero = models.IntegerField()
    cep = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)

class Cliente(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=1000)
    cnpj = models.CharField(max_length=100)
    informacoes_adicionais = models.CharField(max_length=2000)
    descricacao = models.CharField(max_length=5000)
    endereco = models.CharField(max_length=1000)
    numero = models.IntegerField()
    cep = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)

class Orcamento(models.Model):
    codigo = models.AutoField(primary_key=True)
    empresa_jotage = models.ForeignKey(Empresa)
    cliente = models.ForeignKey(Cliente)
    descricacao = models.CharField(max_length=5000)


class OrcamentoXProduto(models.Model):
    id = models.AutoField(primary_key=True)
    orcamento = models.ForeignKey(Orcamento)
    produto = models.ForeignKey(Produto)
    quantidade = models.IntegerField()
    preco_adaptavel = models.DecimalField(max_digits=10, decimal_places=2)
