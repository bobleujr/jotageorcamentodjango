from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models

admin.site.register(models.Produto)
admin.site.register(models.Cliente)
admin.site.register(models.Empresa)
admin.site.register(models.Orcamento)
admin.site.register(models.OrcamentoXProduto)

