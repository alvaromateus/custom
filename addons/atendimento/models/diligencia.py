# -*- coding: utf-8 -*-
from openerp import models, fields

class diligencia(models.Model):
	_name = 'diligencia'
	data = fields.Date('Data')

	descricao = fields.Html('Descrição da diligência')

        assistido_id = fields.Many2one('assistido', string='Assistido')
