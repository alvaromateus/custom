# -*- coding: utf-8 -*-
from openerp import models, fields

class solicitante(models.Model):
	_name = 'solicitante'
	nome = fields.Char('Nome', required=True)
	cpf = fields.Char('CPF')
	rg = fields.Char('RG')
	orgao_emissor = fields.Char('Órgão emissor RG')

	vinculo_assistido = fields.Selection (
		[('esposo','Esposo(a)'),
		('companheiro','Companheiro(a)'),
		('filho','Filho(a)'),
		('pai','Pai'),
		('mae','Mãe'),
		('enteado','Enteado(a)'),
		('tio','Tio(a)'),
		('irmao','Irmão(ã)'),
		('avo','Avô'),
		('avo','Avó'),
		('amigo','Amigo(a)'),
		('padrasto','Padrasto'),
		('madastra','Madastra'),
		('outro','Outros')],
		'Grau de parentesco')

	email = fields.Char('Email')

        assistido_id = fields.Many2one('assistido', string='Assistido')

	telefone = fields.One2many('telefone', 'solicitante_id', string='Telefones')

	endereco = fields.One2many('endereco', 'solicitante_id', string='Endereços')

	atendimento = fields.One2many('atendimento', 'solicitante_id', string='Solicitantes')


	def name_get(self, cr, uid, ids, context=None):
	    if context is None:
		context = {}
	    if isinstance(ids, (int, long)):
		ids = [ids]

	    res = []
	    for record in self.browse(cr, uid, ids, context=context):
		name = record.nome
		cpf = record.cpf
		if cpf == False:
			cpf = "Sem cadastro"
		else:
			cpf = record.cpf
		res.append((record.id, name + " - CPF: " + str(cpf)))
	    return res
