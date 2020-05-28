# -*- coding: utf-8 -*-
from openerp import models, fields, api

class defensor(models.Model):
	_name = 'defensor'
	nome = fields.Char('Nome', required=True)

	atendimento = fields.One2many('atendimento', 'defensor_id', string='Atendimentos')

        sede_id = fields.Many2one('sede', string='Sede/Local', required=True)
	sede = fields.One2many('sede', 'defensor_id', string='Sede coordenada')

	estagio = fields.Boolean('Defensor em estágio probatório')

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
