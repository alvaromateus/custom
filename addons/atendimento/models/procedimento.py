# -*- coding: utf-8 -*-
from openerp import models, fields

class procedimento(models.Model):
	_name = 'procedimento'
	descricao = fields.Char('Descrição', required=True)
#	atendimento = fields.One2many('atendimento', 'atendimento_id', string='Atendimentos')
#        atendimento = fields.Many2one('atendimento', string='Atendimento', required=True)

	atendimento = fields.One2many('atendimento', 'procedimento_id', string='Atendimentos', required=True)

	area = fields.Selection (
		[('criminal','Criminal'),
		('execucao','Execução Penal'),

		('infancia','Infância e Juventude'),

		('extra_judicial','Extrajudicial'),
		('civel_fazenda','Cível / Fazenda Pública'),
		('familia','Família'),
		('violencia_domestica','Violência Doméstica'),
		('curadoria','Curadoria Especial'),

		('cam','Centro de Atendimento Multidisciplinar'),
		('outro','Outros')],'Área do Atendimento')

	def name_get(self, cr, uid, ids, context=None):
	    if context is None:
		context = {}
	    if isinstance(ids, (int, long)):
		ids = [ids]

	    res = []
	    for record in self.browse(cr, uid, ids, context=context):
		name = record.descricao
		res.append((record.id, name))
	    return res
