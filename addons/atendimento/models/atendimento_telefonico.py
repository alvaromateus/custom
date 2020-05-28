# -*- coding: utf-8 -*-
from openerp import models, fields, api

class atendimento_telefonico(models.Model):
	_name = 'atendimento_telefonico'
	
	assistido_id = fields.Many2one('assistido', string='Assistido', required=True)	
	nome_assistido = fields.Char('Nome do assistido',   related='assistido_id.nome')
	
	assessor = fields.Selection (
		[('silvio','Silvio'),
		('mario','Mário'),
		('silvia','Silvia'),
		('tamima','Tamima'),
		('fernanda','Fernanda Van Kan'),
		('fernanda_correa','Fernanda Correa'),
		('flavia','Flávia'),
		('rosa','Rosa')],'Assessor')

		
	nome_solicitante = fields.Char('Nome do solicitante')
	numero_processo = fields.Char('Número do Processo')
	
	telefone = fields.Char('Telefone para retorno')
	
	observacoes = fields.Char('Observações')
	
	realizado = fields.Boolean('Realizado?')

	info = fields.Text('Informações do atendimento')