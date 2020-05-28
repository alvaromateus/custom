# -*- coding: utf-8 -*-
from openerp import models, fields

class telefone(models.Model):
	_name = 'telefone'
	telefone = fields.Char('Telefone', required=True)
	info = fields.Char('Inf. Adicionais')
	tipo = fields.Selection (
		[('celular', 'Celular'),
		('residencial', 'Residencial'),
		('trabalho', 'Trabalho'),
		('outro', 'Outro')])
        assistido_id = fields.Many2one('assistido', string='Assistido')
        solicitante_id = fields.Many2one('solicitante', string='solicitante')
