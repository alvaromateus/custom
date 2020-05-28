# -*- coding: utf-8 -*-
from openerp import models, fields, api

class malote(models.Model):
	_name = 'malote'
	data_cadastro = fields.Date('Data de envio', required=True)
	item = fields.One2many('item', 'malote_id', string='Documentos')

	sede = fields.Selection (
			[('ponta_grossa','Ponta Grossa'),
			('curitiba','Curitiba'), 
			('londrina','Londrina')],
			'Sede')

	para = fields.Selection (
			[('ponta_grossa','Ponta Grossa'),
			('curitiba','Curitiba'), 
			('londrina','Londrina')],
			'Para')

	item = fields.One2many('item', 'malote_id', string='Lista de documentos')

	confirmado = fields.Boolean('Lista de remessa foi devolvida?')

	confirmacao_recebimento = fields.Boolean('Houve confirmação de recebimento?')
	data_confirmacao_recebimento = fields.Date('Data de recebimento da confirmação')
