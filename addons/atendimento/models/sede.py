# -*- coding: utf-8 -*-
from openerp import models, fields, api

class sede(models.Model):
	_name = 'sede'
	nome = fields.Char('Nome', required=True)

	defensor = fields.One2many('defensor', 'sede_id', string='Defensores')
        defensor_id = fields.Many2one('defensor', string='Coordenador')

	atendimento = fields.One2many('atendimento', 'sede_id', string='Atendimentos')
	assistido = fields.One2many('assistido', 'sede_id', string='Assistidos')

	def name_get(self, cr, uid, ids, context=None):
	    if context is None:
		context = {}
	    if isinstance(ids, (int, long)):
		ids = [ids]

	    res = []
	    for record in self.browse(cr, uid, ids, context=context):
		name = record.nome
		res.append((record.id, name))
	    return res
