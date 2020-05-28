# -*- coding: utf-8 -*-
from openerp import models, fields, api

class item(models.Model):
	_name = 'item'
	malote_id = fields.Many2one('malote', string='Malote')

	identificacao = fields.Char('Identificaçao do Documento')
	destino = fields.Char('Nome/setor destinatário')


