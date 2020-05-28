# -*- coding: utf-8 -*-
from openerp import models, fields, api

class antigo(models.Model):
	_name = 'antigo'
	recnum = fields.Char('Recnum')
	ano_pront = fields.Char('Ano Prontuário')
	num_pront = fields.Char('Número Prontuário')
	nome = fields.Char('Nome')
	tipo_cliente = fields.Char('Tipo de Cliente')
	data_cadastro = fields.Char('Data de Cadastro')
	identidade = fields.Char('Identidade')
	ender_resid = fields.Char('Endereço')
	ender_compl = fields.Char('Endereço (complemento)')
	cidade_resid = fields.Char('Cidade')
	estado = fields.Char('Estado')
	fone_contato = fields.Char('Telefone')
	data_nascimento = fields.Char('Data de Nascimento')
	profissao = fields.Char('Profissão')
	cod_reg = fields.Char('Código Registro')
	cep = fields.Char('CEP')
